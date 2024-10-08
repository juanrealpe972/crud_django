from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateTaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {
            'form' : UserCreationForm
        })
    else: 
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(username= request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    'error': 'Username already exists'
                })
        else:
            return render(request, 'signup.html', {
                'form' : UserCreationForm,
                'error': 'Password do not match'
            })

def sign_in(request):
    if request.method == "GET":
        return render(request, 'sign_in.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign_in.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')

@login_required
def tasks(request):
    # tasks =Task.objects.all() #Nos funciona para traer todas las tareas de todos los usuarios
    tasks =Task.objects.filter(user=request.user, date_completed__isnull=True ) #Nos funciona para traer todas mis tareas
    return render(request, 'tasks.html', {
        'tasks': tasks, 
        'title': 'Tasks Pending'
    })

@login_required
def tasks_completed(request):
    tasks =Task.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed') #Nos funciona para traer todas mis tareas
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'title': 'Tasks Completed'
    })

@login_required
def sign_out(request):
    logout(request)
    return redirect('home')

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form' : CreateTaskForm
        })
    else:
        try:
            form = CreateTaskForm(request.POST)
            new_tasks = form.save(commit=False)
            new_tasks.user = request.user
            new_tasks.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form' : CreateTaskForm,    
                'error': 'Please provide valida data'
            })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        # task = Task.objects.get(pk=task_id) #Manera de como se pueden traer los datos de una tarea especifica pero esta en caso de error tumba el servidor
        task = get_object_or_404(Task, pk=task_id, user = request.user)
        form = CreateTaskForm(instance=task)
        return render(request, 'task_detail.html', {
            'task': task,
            'form': form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user = request.user)
            form = CreateTaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks_detail.html', {
                'task': task,
                'form': form,
                'error': 'Error updating task'
            })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.date_completed = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

