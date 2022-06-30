from django.db import models

# Create your models here.

class mod(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)