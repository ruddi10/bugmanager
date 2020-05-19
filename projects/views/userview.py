from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsReporterTeamOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
import requests
# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Issue
from projects.serializers import issueserializer, commentserializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from projects.constants import Client_ID, Client_secret, Redirect_Url, Access_Token_Endpoint, user_data
from projects.models import Profile
from django.contrib.auth import get_user_model

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


User = get_user_model()


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request, pk=None):

        # try:
        #     auth_code = request.data["code"]
        # except KeyError:
        #     return Response("Authentication code not provided", status=status.HTTP_400_BAD_REQUEST)
        # data = {
        #     "client_id": Client_ID,
        #     "client_secret": Client_secret,
        #     "grant_type": "authorization_code",
        #     "redirect_url": Redirect_Url,
        #     "code": auth_code
        # }
        # r = requests.post(Access_Token_Endpoint, data=data).json()
        # if(r.get("errors", None)):
        #     return Response(r, status=status.HTTP_400_BAD_REQUEST)
        # headers = {
        #     'Authorization': 'Bearer ' + r["access_token"],
        # }
        # user_data = requests.get(
        #     url="https://internet.channeli.in/open_auth/get_user_data/", headers=headers).json()
        roles = user_data["person"]["roles"]
        is_maintainer = False
        for role in roles:
            if(role["role"] == "Maintainer"):
                is_maintainer = True
                break

        if(not is_maintainer):
            return Response("You are not allowed", status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(
                enrolment_number=user_data["student"]["enrolmentNumber"])
        except Profile.DoesNotExist:

            user = User.objects.create(
                username=user_data["person"]["fullName"])
            Profile.objects.create(
                User=user, enrolment_number=user_data["student"]["enrolmentNumber"], access_token="abcd")
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_handler(token)

            return Response(response, status=status.HTTP_201_CREATED)
        return Response("succuee")
