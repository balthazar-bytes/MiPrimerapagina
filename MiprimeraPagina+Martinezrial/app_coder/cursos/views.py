from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import Curso,Estudiante,Profesor,Avatar
from .forms import CursoForm,EstudianteForm,ProfesorForm,EditProfileForm,AvatarForm
import sqlite3 as sql
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

# ... (resto de tus importaciones y vistas)



# ... (resto de tus vistas)
'''Apartado de Usuari'''
def perfil(request):    
    return render(request, "cursos/perfil.html", {"usuario": request.user}) 



@login_required
def editarPerfil(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)
        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect("perfil")
    else:
        form = EditProfileForm(instance=request.user)
        if avatar:
            avatar_form = AvatarForm(instance=avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, "cursos/editar_perfil.html", {"form": form, "avatar_form": avatar_form})

# @login_required
# def upload_avatar(request):
#     if request.method == "POST":
#         form = AvatarForm(request.POST, request.FILES,instance=request.user.avatar)
#         if form.is_valid():
#             form.save()
#             return redirect("profile")
#     else:
#         form = AvatarForm(instance=request.user.avatar)
#     return render(request, "cursos/upload_avatar.html", {"form": form})

def registro_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el nuevo usuario
            login(request, user)  # Inicia sesión automáticamente al nuevo usuario
            return redirect("inicio")  # Redirige a la página de inicio después del registro
        else:
            # Si el formulario no es válido, se vuelve a renderizar la página de registro con los errores
            return render(request, "cursos/registro.html", {"form": form, "mensaje": "Por favor, corrige los errores."})
    else:
        form = UserCreationForm()
    # Crea un formulario vacío para una solicitud GET
    return render(request, "cursos/registro.html", {"form": form})




def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                # Puedes redirigir a 'inicio' o a donde prefieras después del login exitoso
                return redirect("inicio") 
            else:
                # Usuario o contraseña incorrectos, renderiza de nuevo login.html con el form que tiene los errores.
                return render(request, "cursos/login.html", {"form": form, "mensaje_error": "Usuario o contraseña incorrectos."})
        else:
            # Formulario no es válido (ej. campos vacíos), renderiza de nuevo login.html con el form que tiene los errores.
            return render(request, "cursos/login.html", {"form": form})
    else: # Para solicitudes GET
        form = AuthenticationForm()
    return render(request, "cursos/login.html", {"form": form})












def inicio(request):
    return render(request, "cursos/inicio.html")


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
'''esto es para mostrar los estudiantes en la vista de estudiantes'''      
class EstudianteListView(ListView):
    model = Estudiante
    template_name = "cursos/estudiantes.html"
    context_object_name = "estudiantes"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset
    
class CursoListView(ListView):
    model = Curso
    template_name = "cursos/cursos.html"
    context_object_name = "cursos"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset
'''esto es para mostrar el detalle de los estudiandes en la vista de estudiantes, tocando el boton de ver detalle''' 
class EstudianteDetailView(DetailView):
    model = Estudiante
    
'''esto es para eliminar los estudiantes en la vista de estudiantes, tocando el boton de eliminar'''
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiantes")

'''esto es para crear un estudiatne en forma de class'''
class EstudainteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    success_url = reverse_lazy("estudiantes")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.nombre = self.request.user
        else:
            form.add_error(None, "Debes iniciar sesión para crear un estudiante.")
            return self.form_valid(form)
        return super().form_valid(form)

'''esto es para actualizar los estudiantes en la vista de estudiantes, tocando el boton de editar'''
#class EstudianteUpdateView(UpdateView):




def editar(request,pk):
    estudiante = Estudiante.objects.get(pk=pk)  # Recupera el estudiante de la base de datos
    
    if request.method == "POST":
        mi_formulario = EstudianteForm(request.POST, instance=estudiante)  # Crea un formulario con los datos del estudiante
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data  # Recupera los datos del formulario
            estudiante.nombre = datos["nombre"]  # Actualiza el nombre del estudiante
            estudiante.apellido = datos["apellido"]  # Actualiza el apellido del estudiante
            estudiante.email = datos["email"]  # Actualiza el email del estudiante
            estudiante.fecha_nacimiento = datos["fecha_nacimiento"]  # Actualiza la fecha de nacimiento del estudiante
            estudiante.save()  # Guarda los cambios en la base de datos
            
            estudiante = Estudiante.objects.all()  # Recupera todos los estudiantes de la base de datos
            return render(request, "cursos/estudiantes.html", {"estudiantes": estudiantes})  # Redirige a la vista de estudiantes
            
    else:
        mi_formulario = EstudianteForm(instance=estudiante)
    return render(request, "cursos/editar_estudiante.html", {"form": mi_formulario, "estudiante": estudiante})


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





