from django.db import models

# Create your models here.

class userfile(models.Model):
	file = models.FileField(upload_to='files/')
	