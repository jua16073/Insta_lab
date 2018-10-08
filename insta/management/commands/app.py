from django.core.management.base import BaseCommand

from django.contrib.auth.models import User

import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    
    #Variables para salir de los ciclos 
    menu1 = True
    menu2 = False
    salir = True

    #info del Usuario ingresado
    usu = None

    while salir:
      while menu1:
        cls()
        print("Hola, este seria el menu :P")
        print("1. Crear Usuario")
        print("2. Listar Usuario")
        print("3. Acceder")
        print("4. Salir")
        opcion = input ("Opcion Seleccionada \n")
        print(opcion)

        if (opcion == "1"):
          cls()
          nombre = input("Ingrese su nombre ")
          apellido = input("Ingrese su apellido ")
          e_mail = input("Ingrese su email ")
          user_name = input("Ingrese su username ")
          new_user = User(first_name = nombre, last_name = apellido, email = e_mail, username = user_name)
          new_user.save()
          print (User.objects.all())
        elif(opcion == "2"):
          cls()
          for user in User.objects.all():
            print("pk = {}: {} {} - {}".format(user.pk, user.first_name, user.last_name, user.username))
        elif(opcion == "3"): 
          cls()
          usuario = input("Ingrese el nombre de usuario ")
          mail = input("Ingrese su email ")
          try:
            ingreso = User.objects.get(username = usuario, email = mail)
            print("Bienvenido" + ingreso.username +" ")
            menu2 = True
            menu1 = False
            usu = ingreso
          except:
            print("Usuario no existe ")
        elif (opcion == "4"):
          cls()
          print("Bye") 
          salir = False
          break

      #Menu para cuando el usuario esta ingresado    
      while menu2:
        print("Bienvenido al menu 2")
        print("1. Crear Post")
        print("2. Like a Post")
        print("3. Borrar Post")
        print("4. Menu Principal")
        
        #input
        opcion = input("Ingrese la opcion escogida ")

        if (opcion == "1"):
          print("Crear post")
          nombre = input("Ingrese el nombre del Post ")
          contenido = input ("Ingrese el contenido del Post")
          
        elif (opcion == "2"):
          print("Likear un post")
        elif (opcion == "3"):
          print("Borrar un post")
        elif (opcion == "4"):
          print("Menu principal")
          menu1 = True
          menu2 = False
          break
        else:
          print ("No escogio una opcion valida")

