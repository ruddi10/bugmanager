from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Projectmodel
from projects.serializers import projectserializers
from rest_framework import generics


class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Projectmodel.Project.objects.all()
    serializer_class = projectserializers.ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Projectmodel.Project.objects.all()
    serializer_class = projectserializers.ProjectSerializer
