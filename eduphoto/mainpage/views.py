# Create your views here.
from datetime import datetime
from django.shortcuts import render

def index(request): 
    plan = 'когда-нибудь потом'
    kogdadata = [27, 6, 2024]
    segodnya = datetime.now()
    segodnya = datetime
    (
        segodnya.year,
        segodnya.month,
        segodnya.day,
    )
#    if kogdadata[0] == segodnya.day and kogdadata[1] == segodnya.month and kogdadata[2] == segodnya.year:
#        plan = 'сегодня'
#    elif kogdadata[0] == (segodnya.day +1) and kogdadata[1] == segodnya.month and kogdadata[2] == segodnya.year:
#        plan = 'завтра'
#    elif kogdadata[0] == (segodnya.day -1) and kogdadata[1] == segodnya.month and kogdadata[2] == segodnya.year:
#        plan = 'вчера'
    return render(
        request,                    # Запрос
	    'mainpage/index.html',
        {
            'kogda': plan,
            'tasks':[ # Они будут получены из базы данных, а не вбиты в код вручную!
                {
                    'description': 'Не опаздывать',
                    'done': True,
                },
                {
                    'description': 'Сделать заглавную страницу',
                    'done': True,
                },
                {
                    'description': 'Лечь спать вовремя',
                    'done': False,
                },
                {
                    'description': 'Починить заглавную страницу',
                    'done': True,
                },
            ]
        }                 
    )


#from templates.tasklist import menu.html
def new_menu(request):
    context = {    }
    return render(
        request,                  # Запрос
	    'mainpage/menu.html', # путь к шаблону
        context
    )