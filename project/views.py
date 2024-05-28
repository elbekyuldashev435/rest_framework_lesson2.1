from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Users
from .serializers import UsersSerializers
# Create your views here.


class UsersAPIView(APIView):
    def get(self, request):
        try:
            users = Users.objects.all()
            serializer = UsersSerializers(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserAPIView(APIView):
    def get(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            serializer = UsersSerializers(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserCreateAPIView(APIView):
    def post(self, request):
        try:
            serializer = UsersSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)


class UserUpdateAPIView(APIView):
    def post(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            serializer = UsersSerializers(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)


class UserDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            user = Users.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_403_FORBIDDEN)