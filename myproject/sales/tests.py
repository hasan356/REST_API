from django.test import TestCase
from rest_framework.test import APITestCase
# Create your tests here.
from django.contrib.auth import get_user_model

from .models import product



    # def test_single_user(self):
    #      user_count = User.objects.count()
    #      self.assertEqual(user_count,1)

    # def test_single_items(self):
    #      items_count = product.objects.count()
    #      self.assertEqual(items_count  ,1)