from django.db import models
from django.conf import settings

from django.db.models.signals import post_save
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

class product(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='itemlists',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    quantity = models.IntegerField()
    pos = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)



# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)