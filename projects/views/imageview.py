from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsReporterTeamOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
from projects.models import Issue, Image
from projects.serializers import issueserializer, commentserializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = commentserializer.ImageSerializer
    permission_classes = [AllowAny]
