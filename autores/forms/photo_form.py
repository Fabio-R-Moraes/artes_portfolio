from django import forms
from portfolio.models import Photos
from utils.django_forms import novos_atributos

class AuthorsPhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        novos_atributos(self.fields.get('historia'), 'class', 'span-2')

    class Meta:
        model = Photos
        fields = 'titulo', 'descricao', 'category', 'preco', 'historia', 'photo_image'

        widgets = {
            'photo_image': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            )
        }