from django.contrib.auth.models import User
from authentication.serializers import UserSerializer, LoginSerializer
from django.db.models.signals import post_save
from rest_framework import permissions
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework import renderers
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import viewsets
from django.db import IntegrityError


class SignUpView(viewsets.ViewSet):
    """
    Signup for users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = self.request.data['username']
            email = self.request.data['email']
            password = self.request.data['password']
            try:
                new_user = User.objects.create_user(
                    username=username, email=email, password=password)
                return Response({'message': 'Registration successful'}, 201)
            except IntegrityError as e:
                return Response({'error': e.message}, 400)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
