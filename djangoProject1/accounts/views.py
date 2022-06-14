from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class LogoutAPIView(APIView):
    pass


# class UserRegistration(generics.CreateAPIView):
#     serializer_class = UserSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class UserRegistration(APIView):
    def post(self, request):
        ser_data = UserSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create_user(username=ser_data.validated_data['username'],
                                     password=ser_data.validated_data['password'],
                                     first_name=ser_data.validated_data['first_name'])
            return Response(data=ser_data.data)
        return Response(data=ser_data.errors)
