from django.urls import path, include
from AppCoder import views
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("fans", views.fans, name="Fans"),
    path("paises_seguidores", views.lideres, name="Paises_seguidores"),
    path("dream_achievers", views.dream_achievers, name="Dream_achievers"),
    path("construyentes", views.construyentes, name="Construyentes"),
    
    path("fansFormulario", views.FansFormulario, name="FansFormulario"),
    path("lideresFormulario", views.lideresFormulario, name="LideresFormulario"),
    path("busquedaCamada", views.busquedaCamada, name="BusquedaCamada"),
    path("buscar/", views.buscar),
    path("leerLideres", views.leerLideres, name="LeerLideres"),
    path("eliminarLideres/<profesor_nombre>", views.eliminarLideres, name="EliminarLideres"),
    path("editarLideres/<lideres_nombre>", views.editarLideres, name="EditarLideres"),
    
    
    
    
    
   
    path("lideres/list/",LideresList.as_view(),name="lideres_list"),
    path('lideres/nuevo/', LideresCreacion.as_view(), name='lideres_crear'),
    path('lideres/<pk>', LideresDetalle.as_view(),name = 'lideres_detalle'),
    path('lideres/editar/<pk>', LideresUptade.as_view(), name='lideres_editar'),
    path('lideres/borrar/<pk>',LideresDelete.as_view(),name='lideres_borrar'),
    
    
    
    
    
    
    
    
    
    path("login",views.login_request, name="Login"),
    path("register", views.register,name="Register"),
    path("logout", LogoutView.as_view(template_name="logout.html"),name="Logout"),
    path("editarPerfil",views.editarPerfil,name="EditarPerfil"),
    path("agregarAvatar", views.agregarAvatar, name="AgregarAvatar"),
    
    
    path('about/', views.about, name='About'),
    path("lista_usuarios/", views.lista_usuarios, name="Lista_Usuarios"),
    path("lista_fans/", views.lista_fans, name="Lista_Fans"),
    
    
    
]

#urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)