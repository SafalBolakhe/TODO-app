from django import forms
from .models import Todo

class MyForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["task",]
        labels = {"task": "To-Do"}