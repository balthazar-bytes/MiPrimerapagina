from django.shortcuts import render,HttpResponse
from .models import Curso,Estudiante,Profesor
from .forms import CursoForm
import sqlite3 as sql

def inicio(request):
    return render(request, "cursos/inicio.html")

def cursos(request):
    return render(request, "cursos/cursos.html")

def estudiantes(request):
    return render(request, "cursos/estudiantes.html")

def profesores(request):
    return render(request, "cursos/profesores.html")

def curso_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        camada = request.POST.get("camada")
        comision = request.POST.get("comision")
        anio = request.POST.get("anio")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")

        if nombre and camada and comision and anio and fecha_inicio and fecha_fin:
            curso = Curso(
                nombre=nombre,
                camada=camada,
                comision=comision,
                anio=anio,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )
            curso.save()
            return render(request, "cursos/inicio.html", {
                "mensaje": "Curso guardado exitosamente"
            })

        return render(request, "cursos/inicio.html", {
            "mensaje": "Todos los campos son obligatorios"
        })

    return render(request, "cursos/inicio.html")

def profesor_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        especialidad = request.POST.get("especialidad")
        
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        

        if nombre and apellido and email  and fecha_nacimiento and especialidad:
            profesor = Profesor(
                nombre=nombre,
                apellido=apellido,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                especialidad=especialidad,
                
            )
            profesor.save()  # Esto guarda el profesor en la base de datos
            return render(request, "cursos/inicio.html", {
                "mensaje": "Profesor guardado exitosamente"
            })

        return render(request, "cursos/inicio.html", {
            "mensaje": "Todos los campos son obligatorios"
        })

    return render(request, "cursos/inicio.html")

def estudiante_form(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")

        if nombre and apellido and email  and fecha_nacimiento :
            estudiante = Estudiante(
                nombre=nombre,
                apellido=apellido,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                
            )
            estudiante.save()  # Esto guarda el estudiante en la base de datos
            return render(request, "cursos/inicio.html", {
                "mensaje": "Estudiante guardado exitosamente"
            })

        return render(request, "cursos/inicio.html", {
            "mensaje": "Todos los campos son obligatorios"
        })

    return render(request, "cursos/inicio.html")
        
        

def estudiantes(request):
    estudiantes = Estudiante.objects.all()  # Recupera todos los estudiantes de la base de datos
    return render(request, "cursos/estudiantes.html", {"estudiantes": estudiantes})
# Create your views here.
def profesores(request):
    profesores = Profesor.objects.all()  # Recupera todos los estudiantes de la base de datos
    return render(request, "cursos/profesores.html", {"profesores": profesores})

def cursos(request):
    cursos = Curso.objects.all()  # Recupera todos los estudiantes de la base de datos
    return render(request, "cursos/cursos.html", {"cursos": cursos})



def buscar_estudiante(request):
    return render(request, "cursos/buscar_estudiante.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request, "cursos/resultados_estudiante.html", {"estudiantes": estudiantes})
    else:
        return HttpResponse("No enviaste datos")
# Create your views here.
