from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length=30)

class Article(models.Model):
    title = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

