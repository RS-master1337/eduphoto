from django.urls import path
from .views import index, new_menu
urlpatterns = [
    path('', index, name='mainpage'),
    path('menu/', new_menu, name='new_menu'),
]