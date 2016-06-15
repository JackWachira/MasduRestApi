from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from authentication.serializers import UserSerializer


class SignUpView(viewsets.ViewSet):
    """ Signup View for users
        Receives a POST with users username,email and password

        Returns status code for registration
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
                User.objects.create_user(
                    username=username, email=email, password=password)
                return Response({'message': 'Registration successful'}, 201)
            except IntegrityError as e:
                return Response({'error': e.message}, 400)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
