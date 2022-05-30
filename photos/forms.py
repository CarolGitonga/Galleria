from django import forms
from django.forms import ModelForm
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

CATEGORIES =( 
    ("1", "Fashion"), 
    ("2", "Superstars"), 
    ("3", "Food"), 
    ("4", "Travel"), 
    ("5", "Nature"), 
    ("6", "Sports"), 
    ("7", "Animals"), 
    
) 


class ImagesForm(forms.Form):
    image = forms.ImageField(required=True) 
    imagename = forms.CharField(required=True)
    description = forms.CharField(required=True)
    locaton = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)