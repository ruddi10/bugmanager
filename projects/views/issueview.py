from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Issue
from projects.serializers import issueserializer
from rest_framework import generics


class IssueList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = issueserializer.IssueSerializer

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)


class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Issue.objects.all()
    serializer_class = issueserializer.IssueUpdateSerializer
