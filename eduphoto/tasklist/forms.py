from django import forms
from .models import Task, Kitten, Photo

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [field.name for field in Task._meta.get_fields()]
        labels = {
            "given": "Задача выдана",
        }
        widgets = {
            'given' :   forms.DateInput(attrs={'type':'datetime-local'}),
            'deadline': forms.DateInput(attrs={'type':'datetime-local'}),
 #          'color': forms.TextInput(attrs={'type':'color'}),
        }


class KittenForm(forms.ModelForm):
    class Meta:
        model = Kitten
        fields = [field.name for field in Kitten._meta.get_fields()]
        widgets = {
            'color': forms.TextInput(attrs={'type':'color'}),
        }   



class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [field.name for field in Photo._meta.get_fields()]
        #widgets = {
        #    'color': forms.TextInput(attrs={'type':'color'}),
        #}   