from django import forms
from portfolio.models import Photos

class AuthorsPhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = 'titulo', 'descricao', 'historia', 'preco', 'photo_image'