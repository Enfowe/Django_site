from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('title')
    return render(request, 'main_app/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main_app/about.html')


def create(request):
    error = ''
    if request == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main_app/create.html', context)
