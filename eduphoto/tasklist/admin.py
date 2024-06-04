from django.contrib import admin 
from .models import Task 
from .models import Kitten
from .models import Photo
  
# Register your models here. 
 
@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Task._meta.get_fields()]
@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Kitten._meta.get_fields()]
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Photo._meta.get_fields()]
