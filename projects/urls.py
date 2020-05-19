from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import projectviews, issueview, commentview, userview
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
router.register(r'project', projectviews.ProjectView)
router.register(r'issues', issueview.IssueView)
router.register(r'comments', commentview.CommentView)
router.register(r'user', userview.UserView)
urlpatterns = [
    path('', include(router.urls)),

    # path('projects/', projectviews.ProjectList.as_view()),
    # path('issues/', issueview.IssueList.as_view()),
    # path('issues/<int:pk>/', issueview.IssueDetail.as_view()),
    # path('projects/<int:pk>/', projectviews.ProjectDetail.as_view()),

]

#urlpatterns = format_suffix_patterns(urlpatterns)
