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
