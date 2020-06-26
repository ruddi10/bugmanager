from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsTeamOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Project
from projects.serializers import projectserializers
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# class ProjectList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Project.objects.all()
#     serializer_class = projectserializers.ProjectSerializer

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)


# class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Project.objects.all()
#     serializer_class = projectserializers.ProjectDetailSerializer
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsTeamOrReadOnly, IsAuthenticated]
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['createdAt', 'title']
    filterset_fields = ['creator']

    def get_serializer_class(self):
        if (self.action == 'list' or self.action == 'create'):
            return projectserializers.ProjectSerializer
        else:
            return projectserializers.ProjectDetailSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
