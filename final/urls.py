"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.contrib.auth.views import *
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',login,{'template_name': 'inicio_sesion.html'},name='login'),
    url(r'^logout/$',logout_then_login,name='logout'),
    url(r'^registrarse/$',Registrarse.as_view(),name='registrarse'), #<--- "Registrarse" es de la clase(form view) que esta en las vistas
    url(r'^$',index_view.as_view(),name='index_view'), #Index_view
    url(r'^ed/$',educacion,name='educacion_view'),
    url(r'^sa/$',salud,name='salud_view'),
    url(r'^se/$',servicio_comunitario,name='servicio_comunitario_view'),
    url(r'^todas/$',todas_categorias,name='todas_categorias_view'),
    url(r'^usuarios/$',usuarios,name='usuarios_view'),
    url(r'^update-perfil/(?P<pk>\d+)/$',update_perfil.as_view(),name='update_perfil'),
    url(r'^update-post/(?P<pk>\d+)/$',update_post.as_view(),name='update_post'),
    url(r'^public/$',publicar_post,name='publicar_post_view'),
    url(r'detail-post/(?P<pk>\d+)/$',detail_post,name="detail_post"),
    url(r'detail-comment/(?P<pk>\d+)/$',detail_comment,name="detail_comment"),
    url(r'^detail-perfil/(?P<pk>\d+)/$',detail_perfil.as_view(),name="detail_perfil"),
    url(r'^delete-post/(?P<pk>\d+)/$',delete_post.as_view(),name='delete_post'),

    url(r'^', include('social_django.urls', namespace='social')),  # <--


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
