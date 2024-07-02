from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True) #El blank funcionar para que al manejar el proyecto a través del administrador (http://127.0.0.1:8000/admin/tasks/task/) Nose deje ingresar un dato como opcional 
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # En caso de que se elimine un usuario, se eliminarán las tareas que el tiene en cascada 

    def __str__(self):
        return self.title + '- by ' + self.user.username
    