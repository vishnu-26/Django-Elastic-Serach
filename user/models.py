from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
