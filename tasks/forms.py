from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before', 'done')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'complete_before': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'})  # Ajuste para un checkbox, si aplica
        }

        