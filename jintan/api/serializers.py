from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model  # will use custom user model

UserModel = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ("username", "password")
