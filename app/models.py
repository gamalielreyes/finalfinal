# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Modelo
#def user_directory_path(instance, filename):
 #   return '{0}/{1}'.format(instance.categoria, filename)

class usuario(models.Model):
    #Tupla de opciones género
    OP_GENERO = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )

    #Tupla de opciones tipo usuario
    OP_TIPO = (
        ('Institucion', 'Institución'),
        ('Persona', 'Persona'),
    )
    
    iduser = models.OneToOneField(User)
    Nombre = models.CharField(max_length=50)
    Apellido_paterno = models.CharField(max_length = 50)
    Apellido_materno = models.CharField(max_length = 50)
    #En la base de datos se guardará la opción como H o M
    Genero = models.CharField(max_length =30, choices = OP_GENERO)
    Edad = models.IntegerField(blank=True, null=True) # Fecha de nacimiento = modelsDateField
    Email = models.EmailField(max_length = 50)
    No_telefono = models.CharField(max_length = 50)
    Direccion = models.CharField(max_length = 100)
    Biografia = models.CharField(max_length = 300)
    #En la base de datos se guardará la opción como I o P
    Tipo_usuario = models.CharField(max_length = 30, choices = OP_TIPO)
    Foto_de_perfil = models.ImageField(upload_to='foto_perfil', blank = True, null=True, default='foto_post/diadoumenos_head_167x197.jpg')

    def __unicode__(self):
        return self.Nombre

class post(models.Model):
    #Tupla de categorías de post
    OP_CATEGORIA = (
        ('Salud', 'Salud'),
        ('Servicio_comunitario', 'Servicio_comunitario'),
        ('Educacion', 'Educacion'),
    )
    
    idpost = models.AutoField(primary_key=True)
    Nombre_post = models.CharField(max_length = 300)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    Informacion = models.CharField(max_length = 200)
    Foto_post = models.ImageField(upload_to='foto_post', blank=True, null=True)
    Fecha_post = models.DateTimeField(default=datetime.now, blank=True)
    #En la base de datos se guardará la opción como S, C o E
    Categoria = models.CharField(max_length = 30, choices = OP_CATEGORIA)

    def __unicode__(self):
        return self.Nombre_post


class sigue(models.Model):
    idsigue = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    idpost = models.ForeignKey('Post', on_delete = models.CASCADE)
    
    def __unicode__(self):
        return self.idsigue


class comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    idpost = models.ForeignKey('Post', on_delete = models.CASCADE)
    texto = models.CharField(max_length = 300)
    fechacomment = models.DateTimeField()
    
    def __unicode__(self):
        return self.texto

class respuesta(models.Model):
    idrespuesta = models.AutoField(primary_key=True)
    idcomentario = models.ForeignKey('Comentario', on_delete = models.CASCADE)
    iduser = models.ForeignKey('Usuario', on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)
    fecharespuesta = models.DateTimeField()
    
    def __unicode__(self):
        return self.idrespuesta