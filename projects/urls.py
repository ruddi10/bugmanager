from django.urls import path
from projects.views import projectviews, issueview
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    path('projects/', projectviews.ProjectList.as_view()),
    path('issues/', issueview.IssueList.as_view()),
    path('issues/<int:pk>/', issueview.IssueDetail.as_view()),
    path('projects/<int:pk>/', projectviews.ProjectDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
