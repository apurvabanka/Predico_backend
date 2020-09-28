from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class user(models.Model):
    # name = models.CharField(max_length=50)
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    position =  models.CharField(max_length=50)
    def __str__(self):
        return self.name

# class salary(models.Model):
# 	name = models.CharField(max_length=50)
# 	salary = models.IntegerField()
	
# 	def __str__(self):
# 		return self.name



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

