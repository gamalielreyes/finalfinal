# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import post_form, formacomentario, Usuario_signup
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
import datetime
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.models import User 
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'index.html')

# Create your views here.
class index_view(TemplateView):
    template_name = 'index.html'

class Registrarse(FormView):
    template_name = 'registrarse.html'
    form_class = Usuario_signup
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        p = usuario()
        p.iduser = user #iduser
        p.Nombre = form.cleaned_data['Nombre']
        p.Apellido_paterno = form.cleaned_data['Apellido_paterno']
        p.Apellido_materno = form.cleaned_data['Apellido_materno']
        p.Genero = form.cleaned_data['Genero']
        #p.Edad = form.cleaned_data['Edad']
        p.Email = form.cleaned_data['Email']
        p.No_telefono = form.cleaned_data['No_telefono']
        p.Direccion = form.cleaned_data['Direccion']
        p.Biografia = form.cleaned_data['Biografia']
        p.Tipo_usuario = form.cleaned_data['Tipo_usuario']
        p.Foto_de_perfil = form.cleaned_data['Foto_de_perfil']
        p.save()
        return super (Registrarse, self).form_valid(form)


def todas_categorias(request):
    tc = post.objects.all().order_by("-Fecha_post")

    query = request.GET.get("q")
    if query:
        tc = tc.filter(
            Q(Nombre_post__icontains = query) |
            Q(Categoria__icontains = query) |
            Q(Informacion__icontains = query) 
            ).distinct()
    return render(request, 'todas_categorias.html',{'list':tc})

def salud(request):
    csalud = post.objects.filter(Categoria = 'Salud').order_by("-Fecha_post")

    query = request.GET.get("q")
    if query:
        csalud = csalud.filter(
            Q(Nombre_post__icontains = query) |
            Q(Informacion__icontains = query) 
            ).distinct()
    return render(request, 'salud.html',{'l1':csalud})

def servicio_comunitario(request):
    cservicio = post.objects.filter(Categoria = 'Servicio_comunitario').order_by("-Fecha_post")
    query = request.GET.get("q")
    if query:
        cservicio = cservicio.filter(
            Q(Nombre_post__icontains = query) |
            Q(Informacion__icontains = query) 
            ).distinct()
    return render(request, 'servicio_comunitario.html',{'l2':cservicio})

def educacion(request):
    ceducacion = post.objects.filter(Categoria = 'Educacion').order_by("-Fecha_post")
    query = request.GET.get("q")
    if query:
        ceducacion = ceducacion.filter(
            Q(Nombre_post__icontains = query) |
            Q(Informacion__icontains = query) 
            ).distinct()
    return render(request, 'educacion.html',{'l3':ceducacion})

def publicar_post(request):
    if  request.method == 'POST':
        form = post_form(request.POST, request.FILES)
        if form.is_valid():
            p = post()
            p.Nombre_post = form.cleaned_data['Nombre_post']
            p.iduser = request.user.usuario
            p.Informacion = form.cleaned_data['Informacion']
            p.Fecha_post = datetime.datetime.now()
            p.Foto_post = form.cleaned_data['Foto_post']
            p.Categoria = form.cleaned_data['Categoria']
            p.save()
            return HttpResponseRedirect('/')
    else:
        form = post_form()
    return render(request, 'publicar_post.html',{'form':form})

def detail_post(request, pk):
    if request.method == "POST":
        form = formacomentario(request.POST)
        if form.is_valid():
            c = comentario()
            c.iduser = request.user.usuario
            c.idpost = post.objects.get(idpost=request.POST.get('Post'))
            c.texto = form.cleaned_data['texto']
            c.fechacomment = datetime.datetime.now()
            c.save()
            p = post.objects.get(idpost=pk)
            context =  {'postobject': p, 'form':form}
            return render(request, 'detail_post.html',context)

    else:
        form = formacomentario()

    p = post.objects.get(idpost=pk)
    context = {'postobject': p, 'form':form}
    return render(request, 'detail_post.html',context)

def detail_comment(request,pk):
    if request.method == 'POST':
        form = formacomentario(request.POST)
        if form.is_valid():
            p = respuesta()
            p.text = form.cleaned_data['texto']
            p.iduser = request.user.usuario
            p.idcomentario = comentario.objects.get(idcomentario=request.POST.get('Comentario'))
            p.fecharespuesta = datetime.datetime.now()
            p.save()
            c = comentario.objects.get(idcomentario=pk)
            form = formacomentario()
            context = {'object':c,'form':form}
            return render(request,'detail_comment.html',context)
    else:
        form = formacomentario()

    p = comentario.objects.get(idcomentario=pk)
    context = {'object':p,'form':form}
    return render(request,'detail_comment.html',context)

class detail_perfil(DetailView):
    model = usuario
    template_name = 'detail_perfil.html'

class update_perfil(UpdateView):
    model = usuario
    fields = ['Nombre','Apellido_paterno','Apellido_materno', 'Genero', 'Edad', 'Email', 'No_telefono', 'Direccion', 'Biografia', 'Tipo_usuario', 'Foto_de_perfil']
    template_name = 'update_perfil.html'
    success_url = reverse_lazy('index_view')

class update_post(UpdateView):
    model = post
    fields = ['Nombre_post', 'Informacion', 'Foto_post', 'Categoria']
    template_name = 'update_post.html'
    success_url = reverse_lazy('index_view')

class delete_post(DeleteView):
    model = post
    fields = "__all__"
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index_view')


def usuarios(request):
    tc = usuario.objects.all()

    query = request.GET.get("q")
    if query:
        tc = tc.filter(
            Q(Nombre__icontains = query) |
            Q(Apellido_paterno__icontains = query) |
            Q(Apellido_materno__icontains = query) |
            Q(Email__icontains = query) |
            Q(No_telefono__icontains = query) |
            Q(Biografia__icontains = query) |
            Q(Tipo_usuario__icontains = query) 
            ).distinct()
    return render(request, 'usuarios.html',{'list':tc})
