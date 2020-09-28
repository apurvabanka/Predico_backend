from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.object.create(user=instance)

class result(models.Model):
    operation = models.CharField(max_length=50)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()
    result2 = models.IntegerField(default=0)
    result3 = models.IntegerField(default=0)
