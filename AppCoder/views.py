from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Fans, Lideres, Avatar
from django.template import Template
from AppCoder.forms import FansFormulario, LideresFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarForumulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen= miFormulario.cleaned_data["imagen"])
            avatar.save()
            
            return render(request, "inicio.html")
        else:
            miFormulario=AvatarFormulario()
        
        return render(request, "agregarAvatar.html",{"miFormulario":miFormulario})
def editarPerfil(request):
    usuario=request.user
    
    if request.method =='POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.last_name=informacion['last_name']
            usuario.first_name=informacion['first_name']
            
            usuario.save()
            
            return render(request, "inicio.html")
    else: 
        miFormulario= UserEditForm(initial={'email': usuario.email})
    return render(request, "editarPerfil.html",{"miFormulario": miFormulario, "usuario":usuario})

def fansFormulario(self):
    fans = Fans(nombre="Desarrollo web", camada="19881")
    fans.save()
    
    documentoDeTexto = f"-----> Fans:{fans.nombre} Camada: {fans.camada}"
    return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,"inicio.html", {'url':avatares[0].imagen.url})

def fans(request):   
    return render(request,"fans.html")

def lideres(request):   
    return render(request,"lideres.html")

def dream_achievers(request): 
    return render(request,"dream_achievers.html")

def construyentes(request):
    return render(request,"construyentes.html")

def fans(request):
    if request.method == "POST":
        miFormulario = FansFormulario(request.POST)#donde llega la inofmracion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            fans  = Fans(nombre=informacion["nombre"],apellido = informacion["apellido"], pais = informacion["pais"])
            fans.save()
            return render(request,"inicio.html")#despues de guardar vuelve a la pagina inicio, sino
    else:
        miFormulario = FansFormulario()
    return render(request,"fans.html", {"miFormulario": miFormulario})#hace esto direcamnte si no es POST osea es get

def lideresFormulario(request):
    if request.method == "POST":
        miFormulario = LideresFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            lideres = Lideres(nombre=informacion["nombre"],
                                apellido=informacion["apellido"],
                                email=informacion["email"],
                                pais=informacion["pais"])
            lideres.save()
            
            return render(request, "inicio.html")
    else:
        miFormulario = LideresFormulario()
        
    return render(request,"lideresFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request,"busquedaCamada.html")

def buscar(request):
    if request.GET['camada']:
        
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada= request.GET['camada']
        fans = Fans.objects.filter(camada__icontains=camada)
        
        return render(request, 'resultadosBusqueda.html', {'fans':fans, 'camada':camada})
    else:
        respuesta= "no enviaste datos."
        
    return HttpResponse(respuesta)

def leerLideres(request):
    lideres = Lideres.objects.all()#trae los profes, todos
    contexto = {"lideres": lideres}
    
    return render(request, 'leerProfesores.html', contexto)

def eliminarLideres(request, lideres_nombre):
    lideres = Lideres.objects.get(nombre=lideres_nombre)
    lideres.delete()
    
    lideres= Lideres.objects.all()
    contexto= {"lidereses:":lideres}
    
    return render(request, "leerLideres.html", contexto)

def editarLideres(request, lideres_nombre):
    lideres= lideres.objects.get(nombre=lideres_nombre)
    
    if request.method == "POST":
        miFormulario = LideresFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            
            lideres.nombre= informacion['nombre']
            lideres.apellido=informacion['apellido']
            lideres.email=informacion['email']
            lideres.pais=informacion['pais']
            
            lideres.save()
            
            return render(request, "inicio.html")
    
    else:
        miFormulario=LideresFormulario(initial={"nombre":lideres.nombre,
                                                 "apellido":lideres.apellido,
                                                 "email":lideres.email, "pais":lideres.pais})
    return render(request,'editarLideres.html', {"miFormulario":miFormulario,"profesor_nombre":lideres_nombre})

class LideresList(ListView):
    model = Lideres
    template_name = "lideres.html"
    
class LideresCreacion(CreateView):
    model = Lideres
    template_name= "crearLideres2.html"
    succes_url= reverse_lazy("lideres_list")
    fields = "__all__"

class LideresDetalle(DetailView):
    model= Lideres
    template_name = "lideresDetalle.html"
    
class LideresUptade(UpdateView):
    model = Lideres
    success_url = reverse_lazy("lideres_list")
    fields = ["nombre", "apellido","email","pais"]
    
class LideresDelete(DeleteView):
    model = Lideres
    success_url = reverse_lazy("lideres_list")
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contras = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contras)
            
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f'Bienvenido {usuario}'})
            else:
                return render(request,"inicio.html",{"mensaje":f'Error,datos erroneo'})
        else:
            return render(request,"inicio.html",{"mensaje":f'Error, formulario erroneo.'})
    form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})

def register(request):
    
    if request.method == "POST":
        
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html",{"mensaje":"Usuario Creado:)"})
    
    else:
        form = UserRegisterForm()
        
    return render(request,"registro.html", {"form":form})


def about(request):
    return render(request, 'about.html')

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def lista_fans(request):
    fans = Fans.objects.all()
    print(fans)
    return render(request, 'lista_fans.html', {'fans': fans})