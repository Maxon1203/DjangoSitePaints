from django import forms
from .models import Painting

class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'description', 'image', 'price', 'size', 'medium']
