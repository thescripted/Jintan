from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions, status

from .serializers import TaskSerializer, UserSerializer
from .models import Task

UserModel = get_user_model()

class TodoListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class UserTodoListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    lookup_field = 'username'

    def get_queryset(self):
        """
        Return a list of all the todos for a user.
        """
        username = self.kwargs['username']
        return Task.objects.filter(owner__username=username)

class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Grab the profile information for the current user.
        """
        current_user = UserModel.objects.get(username=request.user)
        serialized_user = UserSerializer(current_user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
