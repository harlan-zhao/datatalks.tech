from django.db import models

# Create your models here.

class userfile(models.Model):
	time = models.DecimalField(max_digits=31,decimal_places=10)
	