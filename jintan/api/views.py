from django.contrib.auth import get_user_model
from .models import Task
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from .serializers import TaskSerializer, UserSerializer


class LoginView(APIView):
    pass


class LogoutView(APIView):
    pass


class CreateUserView(CreateAPIView):
    """
    Create a new user account. Returns Authentication Token.
    """

    UserModel = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class SessionView(APIView):
    """Determine if the current user is authenticated."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    """Determine who is the current authenticated user."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})

