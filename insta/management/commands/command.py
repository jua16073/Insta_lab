from django.core.management.base import BaseCommand

from insta.models import Post
from insta.models import Likes

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    print ("hola")
    titulo = input("ingrese titulo")
    print (titulo)