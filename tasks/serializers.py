from rest_framework import serializers
from .models import Task, Category
from django.contrib.auth.models import User

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Expose id, username, and email only

# Serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Expose category id and name

# Serializer for Task model
class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)        # Nested user info (read-only)
    category = CategorySerializer(read_only=True) # Nested category info (read-only)

    class Meta:
        model = Task
        fields = '__all__'  # Include all fields from Task model

