# import json
# from channels.generic.websocket import WebsocketConsumer


# class CommentConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def disconnect(self, close_code):
#         pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         self.send(text_data=json.dumps({
#             'message': message
#         }))

import json
from projects.utils import validate_user, refresh_validate
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from projects.models import Comment, Issue
from django.core.exceptions import ObjectDoesNotExist
from projects.serializers import commentserializer


class CommentConsumer(WebsocketConsumer):
    def connect(self):
        self.issue_id = self.scope['url_route']['kwargs']['issue_id']
        self.room_group_name = 'issue_%s' % self.issue_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        if(close_code.get("is_reconnect", None)):

            self.send(json.dumps(
                {"end_message": close_code["content"], "is_reconnect": close_code["is_reconnect"]}))

        else:
            self.send(json.dumps({"end_message": close_code["content"]}))
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        self.close()

    def authenticateUser(self, data):
        token = data.get('token', None)
        if(token):
            try:
                return validate_user(token)
            except:
                try:
                    if(data.get('rtoken', None)):
                        return validate_user(refresh_validate(data['rtoken']))
                except:
                    return None
        return None

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        user = self.authenticateUser(text_data_json)
        if(user):
            try:
                message = text_data_json['message']
                if(not (message and not message.isspace())):
                    self.disconnect(
                        {"content": "Comment cannot be empty", "is_reconnect": True})
                    return None

                issue = Issue.objects.get(id=self.issue_id)
                comment = Comment.objects.create(
                    issue=issue, description=message, commented_by=user)
                serializedComment = commentserializer.CommentSerializer(
                    comment).data
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': serializedComment
                    }
                )
            except KeyError:
                self.disconnect(
                    {"content": "No comment", "is_reconnect": True})
                return None
            except Issue.DoesNotExist:
                self.disconnect({"content": "Invalid Issue"})
                return None

        else:
            self.disconnect({"content": "Not authenticated"})

    # Receive message from room group

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'comment': message
        }))
