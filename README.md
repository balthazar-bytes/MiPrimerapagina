# Plataforma Coder (Proyecto Django)

Este proyecto es una aplicación web desarrollada con Django que sirve como plataforma para la gestión de cursos, estudiantes, profesores, y perfiles de usuario, además de incluir un sistema de mensajería interna.

## Funcionalidades Implementadas

La plataforma cuenta con las siguientes funcionalidades principales:

### 1. Autenticación y Gestión de Usuarios
* **Registro de Nuevos Usuarios**: Permite a los visitantes crear una cuenta en la plataforma.
* **Inicio de Sesión (Login)**: Acceso para usuarios registrados.
* **Cierre de Sesión (Logout)**: Permite a los usuarios salir de su cuenta de forma segura.
* **Visualización de Perfil de Usuario**: Los usuarios pueden ver su propia información de perfil.
    * Muestra nombre de usuario, email, nombre, apellido.
    * Muestra el avatar del usuario si ha sido cargado.
* **Edición de Perfil de Usuario**:
    * Los usuarios pueden modificar su información personal (nombre, apellido, email).
    * Permite cambiar o subir una imagen de **Avatar**.

### 2. Gestión de Cursos
* **Listado de Cursos**: Muestra una lista de todos los cursos disponibles con detalles como nombre, camada, año, comisión y fechas.
* **Creación de Cursos**: Formulario accesible desde la página de inicio para agregar nuevos cursos.

### 3. Gestión de Estudiantes
* **Listado de Estudiantes**: Presenta una lista de todos los estudiantes registrados.
    * Opción de búsqueda dentro del listado.
* **Detalle de Estudiante**: Muestra información detallada de un estudiante específico.
* **Creación de Estudiantes**: Formulario accesible desde la página de inicio (por defecto) o desde el listado de estudiantes para registrar nuevos alumnos.
* **Edición de Estudiantes**: Permite modificar la información de un estudiante existente.
* **Eliminación de Estudiantes**: Permite borrar registros de estudiantes (requiere confirmación).
* **Búsqueda de Estudiantes**: Funcionalidad para buscar estudiantes por nombre.

### 4. Gestión de Profesores
* **Listado de Profesores**: Muestra una lista de los profesores con su información y especialidad.
* **Creación de Profesores**: Formulario accesible desde la página de inicio para agregar nuevos profesores.

### 5. Página de Inicio (Dashboard de Formularios)
* La página principal (`/`) actúa como un panel central donde se puede acceder a los formularios para crear Cursos, Profesores o Estudiantes.
* Por defecto, el formulario de "Alumno" (Estudiante) es el primero en mostrarse.

### 6. Sistema de Mensajería Interna (App: `mensajes`)
* **Bandeja de Entrada**: Lista las conversaciones activas del usuario, ordenadas por el mensaje más reciente y mostrando mensajes no leídos.
* **Vista de Chat**: Permite ver el historial de mensajes con otro usuario y enviar nuevos mensajes. Los mensajes se marcan como leídos al abrir el chat.
* **Iniciar Nuevo Chat**: Página para seleccionar un usuario de una lista y comenzar una nueva conversación.

### 7. Interfaz de Usuario
* **Modo Oscuro**: Un interruptor en la barra de navegación permite al usuario alternar entre el tema claro y oscuro. La preferencia se guarda en el navegador del usuario (`localStorage`).
* **Diseño Responsivo**: Utiliza Bootstrap 5 para una visualización adaptable en diferentes dispositivos.
* **Navegación Condicional**: Algunos enlaces en la barra de navegación (como "Estudiantes") pueden mostrarse u ocultarse dependiendo de si el usuario ha iniciado sesión o no.
