import email
from email.policy import default
from pyexpat import model
# from unittest import signals
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.BigIntegerField()


def upload_profile_to(instance, filename):
    return f'profile_picture/{instance.user.username}/{filename}'


def upload_cover_to(instance, filename):
    return f'coverImage/{instance.user.username}/{filename}'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	gen = (('--', '------'),('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
	about_me = models.CharField(max_length=250, blank=True)
	profile_pic = models.ImageField(upload_to = 'profile', default="images/default_profile_pic.png")
	gender = models.CharField(choices=gen, max_length=6, null=True)
	created_on = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)