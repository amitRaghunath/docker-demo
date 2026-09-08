from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(ModelViewSet):
    http_method_names = ['post', 'put', 'patch', 'delete', 'get']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        print("Local changes Done", flush=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
