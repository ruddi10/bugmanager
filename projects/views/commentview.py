from rest_framework import permissions
# Create your views here.
from projects.models import Comment
from projects.serializers import commentserializer
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsCommentorOrReadOnly
from rest_framework.permissions import IsAuthenticated

# class IssueList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Issue.objects.all()
#     serializer_class = issueserializer.IssueSerializer

#     def perform_create(self, serializer):
#         serializer.save(reporter=self.request.user)


# class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Issue.objects.all()
#     serializer_class = issueserializer.IssueUpdateSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsCommentorOrReadOnly, IsAuthenticated]
    serializer_class = commentserializer.CommentSerializer

    # def get_serializer_class(self):
    #     if (self.action == 'list' or self.action == 'create'):
    #         return issueserializer.IssueSerializer
    #     else:
    #         return issueserializer.IssueUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(commented_by=self.request.user)

    # def get_serializer_context(self):
    #     context = super(IssueView, self).get_serializer_context()
    #     context.update({"request": self.request})
    #     return context
