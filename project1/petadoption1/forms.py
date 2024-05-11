from django import forms
from petadoption1.models import Pet

class CreatePetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ['petname', 'breed', 'description', 'price', 'url', 'pet_category']