from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre


# python manage.py makemigrations
# python manage.py migrate
#python manage.py runserver