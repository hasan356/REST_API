from django.shortcuts import render

from rest_framework import generics
from .serialize import salesSerializers,UserSerializer
from .models import product
from .permission import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class createview(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = salesSerializers
    queryset = product.objects.all()

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(user = self.request.user)  # Add owner=self.request.user


class crudview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = salesSerializers
    queryset = product.objects.all()

# Create your views here.

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer