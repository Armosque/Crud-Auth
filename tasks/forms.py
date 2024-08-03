from . models import Task
from django import forms



class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("title", "description", "important")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add new task'}),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Add new description',
                    'rows': 3,'style':
                    'resize: both; overflow: hidden;'
                    }),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
