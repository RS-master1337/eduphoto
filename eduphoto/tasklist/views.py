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


from .models import Kitten
def look_for(request):
    if request.method == "POST":
#       form = KittenForm(request.POST, request.FILES)
        print(request.POST)
   #     print(request.POST['Catname'][0])
        print(request.POST.get('Catname'))
        context = {'kittens': 'KittensNotFound'}
        kittens_found = Kitten.objects.filter(imya=request.POST.get('Catname'))
        if kittens_found: #Если котята найдены, список QuerySet [] не будет пустым и не будет ложным, в питоне все пустое - ложное, но не является False!
            context = {
                'kittens': list(kittens_found)
            }
        else:
            print('проверка котенка', list(kittens_found))
        print(len(kittens_found))

        return render(
            request,                         # Запрос
	        'tasklist/kotenok_render.html',  # путь к шаблону
            context                          # подстановки
        )
#        if form.is_valid():
#            print(form.cleaned_data)
#            form.save()
    #else:
    context = {
        
    }
    return render(
        request,                  # Запрос
	    'tasklist/lookfor.html',  # путь к шаблону
        context                   # подстановки
    )

#Bublik
#{'csrfmiddlewaretoken': ['RJYDd9RAsCgNKncyoWDY0zkcFnCbKPlQqIvgf4IowY8jNuGDmfQuErAqusEgmof9'], 'Catname': ['Вася']}


def aboutus(request):
    return render(
        request,                  # Запрос
	    'tasklist/aboutus.html',# путь к шаблону
    )


def stranichka(request):
    return render(  
        request,               # Запрос
	    'tasklist/empty.html',  # путь к шаблону                  # подстановки
    )