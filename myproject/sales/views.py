from django.shortcuts import render

from rest_framework import generics
from .serialize import salesSerializers
from .models import product
from .permission import IsOwnerOrReadOnly
class createview(generics.ListCreateAPIView):

    serializer_class = salesSerializers
    queryset = product.objects.all()


class crudview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = salesSerializers
    queryset = product.objects.all()

# Create your views here.
