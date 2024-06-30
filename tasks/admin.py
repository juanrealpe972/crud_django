from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', ) #Aqui se pueden agregar los campos que queramos que aparezcan en el panel de administrador

# Register your models here.
admin.site.register(Task, TaskAdmin) #Se instancia y de agrega la clase creada para mostrar el campo de created
