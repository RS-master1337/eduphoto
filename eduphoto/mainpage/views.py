# Create your views here.

from django.shortcuts import render
def index(request):
    return render(
        request,                    # Запрос
	    'mainpage/index.html',      # путь к шаблону
        #context                    # подстановки
    )
