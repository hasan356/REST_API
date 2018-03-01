from django.shortcuts import render

from rest_framework import generics
from .serializer import salesListSerializers, salesDetailSerializers
from .models import product
from .permission import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter



class SalesListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = product.objects.all()
    serializer_class = salesListSerializers
    filter_backends = [SearchFilter]
    search_fields = ['name', 'pos', 'user__first_name']


class SalesCreateView(generics.CreateAPIView):
    queryset = product.objects.all()
    serializer_class = salesListSerializers
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class SalesDetailView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = salesDetailSerializers
    permission_classes = [AllowAny]

class SalesUpdateView(generics.RetrieveUpdateAPIView):
    queryset = product.objects.all()
    serializer_class = salesListSerializers
    permission_classes = [IsOwnerOrReadOnly]


class SalesDeleteView(generics.RetrieveDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = salesListSerializers
    permission_classes = [IsOwnerOrReadOnly]
# Create your views here.

