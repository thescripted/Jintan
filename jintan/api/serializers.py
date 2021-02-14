from rest_framework import serializers
from django.contrib.auth import get_user_model  # will use custom user model
from .models import Task

UserModel = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login')
