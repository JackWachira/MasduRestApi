from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, max_length=100, write_only=True)
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, max_length=100, write_only=True)
    email = serializers.EmailField(max_length=100, required=True)
    username = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'confirm_password')
        read_only_fields = ('id', 'confirm_password')

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)

    def validate(self, data):
        if data['password']:
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError(
                    "The passwords have to be the same"
                )
        return data


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, max_length=100, write_only=True, required=True)
    email = serializers.EmailField(
        max_length=100, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        read_only_fields = ('id',)
