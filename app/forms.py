# coding=utf-8
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#clases
class post_form (forms.ModelForm):
    Foto_post = forms.ImageField(required=False)

    class Meta:
        model = post
        exclude = ['idpost', 'iduser', 'Fecha_post']

class formacomentario (forms.Form):
    texto = forms.CharField(max_length = 200)


class Usuario_signup (UserCreationForm):
    OP_GENERO = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    OP_TIPO = (
        ('Persona', 'Persona'),
        ('Institucion', 'Institución'),
    )

    Nombre = forms.CharField(max_length = 50)
    Apellido_paterno = forms.CharField(max_length = 50)
    Apellido_materno = forms.CharField(max_length = 50)
    #En la base de datos se guardara la opcion como H o M
    Genero = forms.ChoiceField(choices = OP_GENERO)
    #Edad = forms.IntegerField(required=False) #Fecha de nacimiento = formsDateField
    Email = forms.EmailField(max_length = 50)
    No_telefono = forms.CharField(max_length = 50)
    Direccion = forms.CharField(max_length = 100)
    Biografia = forms.CharField(max_length = 300)
    #En la base de datos se guardara la opcion como I o P
    Tipo_usuario = forms.ChoiceField(choices = OP_TIPO)
    Foto_de_perfil = forms.ImageField()


  