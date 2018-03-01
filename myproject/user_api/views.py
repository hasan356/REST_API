from rest_framework import generics
from .serializer import UserCreateSerializer,UserLoginSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter
from django.contrib.auth import get_user_model

User = get_user_model()

 #Creating the user registration view

class UserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

#Creating the user login View

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self , request , *args , **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data , HTTP_200_OK)

        return Response(serializer.errors , HTTP_400_BAD_REQUEST)
