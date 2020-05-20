from django.shortcuts import render
from rest_framework import viewsets
from projects.permissions import IsReporterTeamOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
import requests
import json
# Create your views here.
from rest_framework import permissions
# Create your views here.
from projects.models import Issue
from projects.serializers import issueserializer, commentserializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from projects.constants import Client_ID, Client_secret, Redirect_Url, Access_Token_Endpoint
from projects.models import Profile
from django.contrib.auth import get_user_model
from projects.utils import get_tokens_for_user


User = get_user_model()


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request, pk=None):

        try:
            auth_code = request.data["code"]
        except KeyError:
            return Response("Authentication code not provided", status=status.HTTP_400_BAD_REQUEST)
        data = {
            "client_id": Client_ID,
            "client_secret": Client_secret,
            "grant_type": "authorization_code",
            "redirect_url": Redirect_Url,
            "code": auth_code
        }
        r = requests.post(Access_Token_Endpoint, data=data).json()
        if(r.get("error", None)):
            return Response(r, status=status.HTTP_400_BAD_REQUEST)
        headers = {
            'Authorization': 'Bearer ' + r["access_token"]
        }
        user_data = requests.get(
            url="https://internet.channeli.in/open_auth/get_user_data/", headers=headers).json()
        roles = user_data["person"]["roles"]
        is_maintainer = False
        for role in roles:
            if(role["role"] == "Maintainer"):
                is_maintainer = True
                break

        if(not is_maintainer):
            return Response("You are not allowed", status=status.HTTP_403_FORBIDDEN)
        try:
            profile = Profile.objects.get(
                enrolment_number=user_data["student"]["enrolmentNumber"])
        except Profile.DoesNotExist:
            username = f'{user_data["person"]["fullName"].split()[0]}_{user_data["userId"]}'
            user = User.objects.create(
                username=username)
            Profile.objects.create(
                User=user, enrolment_number=user_data["student"]["enrolmentNumber"], access_token=r["access_token"], full_name=user_data["person"]["fullName"], email=user_data["contactInformation"]["emailAddress"])
            response = get_tokens_for_user(user)
            return Response(response, status=status.HTTP_201_CREATED)
        profile.access_token = r["access_token"]
        profile.full_name = user_data["person"]["fullName"]
        profile.email = user_data["contactInformation"]["emailAddress"]
        user = profile.User
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_202_ACCEPTED)
