from django.urls import path
from .views import index, new_task, new_kitten, new_photo

urlpatterns = [
    path('', index),
    path('newtask/', new_task, name='new_task'),
    path('newkitten/', new_kitten, name='new_kitten'),
    path('newphoto/', new_photo, name='new_photo'),
]