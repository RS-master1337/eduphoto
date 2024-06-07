# Create your views here.

from django.shortcuts import render
from datetime import datetime
def index(request):
    context = {
        'tasks':[
            {
                'done':False,
            }
        ]
    }
    return render(
        request,                   # Запрос
	    'tasklist/index.html',     # путь к шаблону
        {
            'task_number': 5
        },
        {
            'vremya': datetime.now
        }
        #context                    # подстановки
    )


from .forms import TaskForm

def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': TaskForm(),
    }
    return render(
        request,                  # Запрос
	    'tasklist/newtask.html',  # путь к шаблону
        context                   # подстановки
    )

from .forms import KittenForm
def new_kitten(request):
    if request.method == "POST":
        form = KittenForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': KittenForm(),
    }
    return render(
        request,                  # Запрос
	    'tasklist/newkitten.html',# путь к шаблону
        context                   # подстановки
    )


from .forms import PhotoForm
def new_photo(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': PhotoForm(),
    }
    return render(
        request,                  # Запрос
	    'tasklist/newphoto.html', # путь к шаблону
        context                   # подстановки
    )
