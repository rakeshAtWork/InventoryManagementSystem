from .models import *
# serializers.py

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Incorrect username or password")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'")

        data['user'] = user
        return data


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['name', 'age']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age should be greater than 18")
        return data
