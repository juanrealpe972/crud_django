from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CreateTaskForm

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
        
def tasks(request): 
    return render(request, 'tasks.html')

def sign_out(request):
    logout(request)
    return redirect('home')

def sign_in(request):
    if request.method == "GET":
        return render(request, 'sign_in.html', {
            'form' : AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user == None :
            return render(request, 'sign_in.html', {
                'form' : AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')

def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {
            'form' : CreateTaskForm
        })
    else:
        print(request.POST)
        return render(request, 'create_task.html', {
            'form' : CreateTaskForm
        })