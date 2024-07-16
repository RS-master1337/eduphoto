from django.urls import path
from .views import index, new_task, new_kitten, new_photo, look_for, aboutus, stranichka
 
urlpatterns = [
    path('', index),
    path('newtask/', new_task, name='new_task'),
    path('newkitten/', new_kitten, name='new_kitten'),
    path('newphoto/', new_photo, name='new_photo'),
    path('lookfor/', look_for, name= 'lookfor'),
    path('aboutus/', aboutus, name='aboutus'),
    path('json/', stranichka, name ='stranichka')
]