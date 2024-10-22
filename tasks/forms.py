from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply Bootstrap class to all visible fields
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before', 'done')  # Add 'done' to fields
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control'}),
            'complete_before': forms.widgets.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})  # Style the complete_before field
            # For 'done', we'll handle the checkbox in the template
        }
