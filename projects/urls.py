from django.urls import path
from projects.views import projectviews
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    path('projects/', projectviews.ProjectList.as_view()),
    path('projects/<int:pk>/', projectviews.ProjectDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
