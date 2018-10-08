from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from insta.models import Post
from insta.models import Likes

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
        cls()
        print("Bienvenido al menu de "+ usu.username)
        print("1. Crear Post")
        print("2. Like a Post")
        print("3. Borrar Post")
        print("4. Menu Principal")
        
        #input
        opcion = input("Ingrese la opcion escogida ")

        if (opcion == "1"):
          cls()
          print(Post.objects.all().count())
          print("Crear post")
          nombre = input("Ingrese el nombre del Post ")
          contenido = input ("Ingrese el contenido del Post")
          new_post = Post(titulo = nombre, idUsu = usu, content = contenido)
          new_post.save()
          print(Post.objects.all())
          print(Post.objects.all().count())
        elif (opcion == "2"):
          cls()
          print("Likear un post")
          for x in Post.objects.all():
            print(str(x.id) + "  "+ x.titulo +" " + str(Likes.objects.filter(idPost = x).count())+"\n"+ str(x.fecha)+"\n\n"+ x.content+"\n-------------------------------\n\n" )
          idB = input("Ingrese el id del post que quiere buscar likear")
          print(idB)
          try:
            post = Post.objects.get(id= idB)
            new_like = Likes(usuario = usu, idPost= post)
            new_like.save()
            input("Exito")
          except:
            print("hey, algo fallo")
            input("...")
        elif (opcion == "3"):
          cls()
          print("Borrar un post")
          for x in Post.objects.filter(idUsu = usu):
            print(str(x.id) + "  "+ x.titulo +" " + str(Likes.objects.filter(idPost = x).count())+"\n"+ str(x.fecha)+"\n\n"+"-------------------------------\n\n" )
          post_borrar = input("Ingrese el id del post a borrar")
          try:
            borrar_post = Post.objects.get(id=post_borrar)
            borrar_post.delete()
            input("Exito ")
          except:
            input("whooops, algo fallo ")
        elif (opcion == "4"):
          cls()
          print("Menu principal")
          menu1 = True
          menu2 = False
          usu = None
          break
        else:
          print ("No escogio una opcion valida")

