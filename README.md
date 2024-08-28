# TaskTrack

TaskTrack es una aplicación web diseñada para facilitar la gestión y organización de tareas. Permite a los usuarios crear, leer, actualizar y eliminar (CRUD) tareas de manera eficiente. La aplicación está desarrollada con Django para la lógica del servidor y la gestión de datos, y Bootstrap para crear una interfaz de usuario atractiva y responsiva.

## Requisitos

- Python 3.6 o superior
- Django 3.2 o superior
- Bootstrap 4 o superior

## Instalación

Sigue estos pasos para clonar y configurar el proyecto:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/juanrealpe972/crud_django.git

2. **Accede al directorio del proyecto:**

   ```bash
    cd crud_django

3. **Crea un entorno virtual e instálalo:**

   ```bash
    python -m venv env
    source env/bin/activate   # Para Linux/MacOS
    env\Scripts\activate      # Para Windows

4. **Instala las dependencias:**

   ```bash
    pip install -r requirements.txt

5. **Configura la base de datos:**

    Abre settings.py y encuentra las líneas 83-86. Asegúrate de que se vean así:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

6. **Realiza las migraciones:**

   ```bash
    python manage.py migrate

7. **Crea un superusuario para acceder al panel de administración:**

   ```bash
    python manage.py createsuperuser

    Sigue las instrucciones para crear el superusuario.

8. **Inicia el servidor de desarrollo:**

   ```bash
    python manage.py runserver

Uso

La aplicación estará disponible localmente en http://127.0.0.1:8000/ y también en línea en https://django-projects-u6rw.onrender.com/.

Panel de Administración: Accede a http://127.0.0.1:8000/admin para gestionar usuarios y otras configuraciones del sistema.

## Photo

### TaskTrack-PC
**Visualización de la web de TaskTrack en PC.**  
![TaskTrack-PC](https://co.pinterest.com/pin/618752436351392093/)

### TaskTrack-Móvil
**Visualización de la web de TaskTrack en dispositivos móviles.**  
![TaskTrack-Móvil](https://co.pinterest.com/pin/618752436351392092/)

### TaskTrack-Tablet
**Visualización de la web de TaskTrack en tabletas.**  
![TaskTrack-Tablet](https://co.pinterest.com/pin/618752436351392095/)
