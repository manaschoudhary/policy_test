from django.forms import ModelForm
from .models import phase_1
from django import forms
# our new form

class phase_1Form(forms.ModelForm):
    class Meta:
        model = phase_1
        fields =('problem_images','problem_images_upload',)
