import email
from django.db import models
from PIL import Image
# Create your models here.

class Slider(models.Model):
	name = models.CharField(max_length=50, default = "", null=True)
	image = models.ImageField(upload_to='slider_img')

	def __str__(self):
		return f'{self.name}'

class Contact(models.Model):
	email = models.EmailField()
	content = models.CharField(max_length=99999)

class Category(models.Model):
	name = models.CharField(max_length=99)
	image = models.ImageField(upload_to="category_images/")

	def __str__(self) -> str:
		return self.name