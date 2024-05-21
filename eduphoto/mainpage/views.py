# Create your views here.
from datetime import datetime
from django.shortcuts import render
def index(request):
    return render(
        request,                    # Запрос
	    'mainpage/index.html',
        {
            'kogda': datetime.now().strftime('%Y %B %d'),
            'chto':[ # Они будут получены из базы данных, а не вбиты в код вручную!
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
            ]
        }                 
    )
