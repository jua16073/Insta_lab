from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  titulo = models.CharField(max_length=50)
  idUsu = models.ForeignKey(User, null = False, on_delete= models.CASCADE)
  content = models.CharField(max_length= 500)
  fecha = models.DateTimeField(auto_now_add = True)


class Likes(models.Model):
  usuario = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
  idPost = models.ForeignKey(Post,null = False, on_delete= models.CASCADE)
  fecha = models.DateTimeField(auto_now_add = True)
  