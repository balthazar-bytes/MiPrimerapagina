from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
   # path("cursos/", views.cursos, name="cursos"),
    #path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("estudiantes/", views.EstudianteListView.as_view(), name="estudiantes"),
    path ("cursos/", views.CursoListView.as_view(), name="cursos"),
    path("profesores/", views.profesores, name="profesores"),
    path("curso_form/", views.curso_form, name="curso_form"),
    path("profesor_form/", views.profesor_form, name="profesor_form"),
    path("estudiante_form/", views.estudiante_form, name="estudiante_form"),
    path("buscar_estudiante/", views.buscar_estudiante, name="buscar_estudiante"),
    path("resultados_estudiante/", views.buscar, name="buscar"),
    path("estudiante/detail/<int:pk>", views.EstudianteDetailView.as_view(), name="estudiante_detail"),
    path("estudiante/delete/<int:pk>", views.EstudianteDeleteView.as_view(), name="estudiante_delete"),
    path("estudiante/update/<int:pk>", views.editar, name="editar_estudiante"),
    path("",views.login_request, name="Login"),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editarPerfil, name='editar_perfil'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    

]
