from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

class Command(BaseCommand):
  def handle(self, *args, **kwargs):

    while True:
      print("Hola, este seria el menu :P")
      print("1. Crear Usuario")
      print("2. Listar Usuario")
      print("3. Acceder")
      print("4. Salir")
      opcion = input ("Opcion Seleccionada\n")
      print(opcion)

      if (opcion == "1"):
        cls()
        nombre = input("Ingrese su nombre")
        apellido = input("Ingrese su apellido")
        e_mail = input("Ingrese su email")
        user_name = input("Ingrese su username")
        new_user = User(first_name = nombre, last_name = apellido, email = e_mail, username = user_name)
        new_user.save()
        print (User.objects.all())
      elif(opcion == "2"):
        cls()
        for user in User.objects.all():
          print("pk = {}: {} {} - {}".format(user.pk, user.first_name, user.last_name, user.username))
      elif(opcion == "3"): 
        cls()
        usuario = input("Ingrese el nombre de usuario")
        mail = input("Ingrese su email")
        try:
          ingreso = User.objects.get(username = usuario, email = mail)
          print("Bienvenido" + ingreso.username)
        except:
          print("Usuario no existe")
      elif (opcion == "4"):
        cls()
        print("Bye") 
        break;