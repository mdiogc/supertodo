from django import forms

from .models import Task


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ('name', 'description')
        widgets = {'title': forms.widgets.TextInput(attrs={'class': 'form-control'})}
