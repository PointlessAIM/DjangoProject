from django.db import models

# Cada vez que hagamos cambios en el modelo, debemos ejecutar el comando
# python manage.py makemigrations <nombre de la app> (para crear las migraciones)
# python manage.py migrate (para aplicar las migraciones)
class Post(models.Model):
    # En este modelo se definen los campos de la base de datos,
    # las caracteristicas que podemos crear y editar

    title = models.CharField(max_length=250)
    content = models.TextField()
    
    # Si no definimos esta funcion, cuando se muestre el objeto en el navegador, se va a
    # mostrar el objeto en memoria, y no el titulo del post 
    def __str__(self):
        return self.title