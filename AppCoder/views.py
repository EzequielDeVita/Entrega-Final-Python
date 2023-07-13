from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.http import HttpResponse
from django.template import Template
from AppCoder.forms import CursoFormulario, ProfesorFormulario

# Create your views here.

def cursoFormulario(self):
    curso = Curso(nombre="Desarrollo web", camada="19881")
    curso.save()
    
    documentoDeTexto = f"-----> Curso:{curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request,"inicio.html")

def cursos(request):   
    return render(request,"cursos.html")

def profesores(request):   
    return render(request,"profesores.html")

def estudiantes(request): 
    return render(request,"estudiantes.html")

def entregables(request):
    return render(request,"entregables.html")

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)#donde llega la inofmracion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            curso  = Curso(nombre=informacion["nombre"],camada = informacion["camada"])
            curso.save()
            return render(request,"inicio.html")#despues de guardar vuelve ala pagina inicio, sino
    else:
        miFormulario = CursoFormulario()
    return render(request,"cursos.html", {"miFormulario": miFormulario})#hace esto direcamnte si no es POST osewa es get

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            profesor = Profesor(nombre=informacion["nombre"],
                                apellido=informacion["apellido"],
                                email=informacion["email"],
                                profesion=informacion["profesion"])
            profesor.save()
            
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario()
        
    return render(request,"profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request,"busquedaCamada.html")

def buscar(request):
    if request.GET['camada']:
        
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada= request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, 'resultadosBusqueda.html', {'cursos':curso, 'camada':camada})
    else:
        respuesta= "no enviaste datos."
        
    return HttpResponse(respuesta)