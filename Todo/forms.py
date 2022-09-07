from django import forms
from .models import tsk


class Taskform(forms.ModelForm):
    class Meta:
         model=tsk
         fields=('Task','status',)
         

   