from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("profesores/", views.profesores, name="profesores"),
    path("curso_form/", views.curso_form, name="curso_form"),
    path("profesor_form/", views.profesor_form, name="profesor_form"),
    path("estudiante_form/", views.estudiante_form, name="estudiante_form"),
    path("buscar_estudiante/", views.buscar_estudiante, name="buscar_estudiante"),
    path("resultados_estudiante/", views.buscar, name="buscar"),
]