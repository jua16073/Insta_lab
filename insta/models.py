from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  titulo = models.CharField(max_length=50)
  idUsu = models.ForeignKey(User, null = True, on_delete= models.SET_NULL)
  content = models.CharField(max_length= 200)

class Likes(models.Model):
  idUsu = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
  likes = models.IntegerField()
  fecha = models.DateTimeField()