from django.test import TestCase

from .models import Curso, Estudiante, Profesor, Avatar

Estudiante1 = Estudiante


class AlumnoTestCase(TestCase):
    def setUp(self):
        Estudiante.objects.create(nombre="Juan", apellido="Perez", email="",fecha_nacimiento="2000-01-01")
    
    def test_alumno_creation(self):
        """Test that an Estudiante can be created successfully."""
        alumno = Estudiante.objects.get(nombre="Juan")
        self.assertEqual(alumno.apellido, "Perez")
        self.assertEqual(alumno.email, "")
        self.assertIsInstance(alumno, Estudiante)

    
# Create your tests here.



