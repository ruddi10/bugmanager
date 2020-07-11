from rest_framework import viewsets
from projects.models import Tag
from rest_framework.permissions import IsAuthenticated
from projects.serializers import tagserializer


class TagView(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = tagserializer.TagSerializer
    pagination_class = None
