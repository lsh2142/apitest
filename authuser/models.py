from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.EmailField(unique=True, null=False, max_length=254)
    isMaasParticipant = models.BooleanField(default=False)
    # ...


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ReservationData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.CharField(max_length=3, null=False)
    code = models.CharField(max_length=3, null=False)
    date = models.CharField(max_length=14, null=False)
    depart = models.TextField(null=False)
    dest = models.TextField(null=False)
    sn = models.TextField(null=True)
