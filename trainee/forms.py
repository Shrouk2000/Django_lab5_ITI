# myapp/forms.py
from django import forms
from .models import Trainee

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'age', 'progress']
