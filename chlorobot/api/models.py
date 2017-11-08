from django.db import models
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Sensor(models.Model) :
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    gpio = models.IntegerField(blank=False, null=False)


class State(models.Model) :
    sensor = models.ForeignKey(sensor)
    value = models.CharField(max_longth=255, blank=False, null=False)
    created_time = models.DateTimefield(auto_now_add=True)


