from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsReporterTeamOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Issue
from projects.serializers import issueserializer, commentserializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


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


class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    permission_classes = [IsReporterTeamOrReadOnly, IsAuthenticated]

    def get_serializer_class(self):
        if (self.action == 'list' or self.action == 'create'):
            return issueserializer.IssueSerializer
        else:
            return issueserializer.IssueUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

    def get_serializer_context(self):
        context = super(IssueView, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    # @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    # def add_comment(self, request, pk=None):
    #     request.data['issue'] = self.get_object().id
    #     request.data['commented_by'] = request.user.username
    #     serializer = commentserializer.CommentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
