from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.forms import ValidationError
from collections import defaultdict
from django.utils.translation import gettext_lazy as _

class PhotosManager(models.Manager):
    def get_publicados(self):
        return self.filter(
            esta_publicado = True,
        ).annotate(
            author_name_complete = Concat(
                F('author__first_name'),
                Value(''),
                F('author__last_name'),
                Value('('),
                F('author__username'),
                Value(')')
            )
        ).order_by('-id')
    
class Category(models.Model):
    nome =  models.CharField('Categoria', max_length=65)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Photos(models.Model):
    objects = PhotosManager()
    titulo = models.CharField('Título', max_length=65)
    descricao = models.CharField('Descrição', max_length=165)
    slug = models.SlugField(unique=True)
    historia = models.TextField('História',)
    historia_html = models.BooleanField(default=False)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    esta_publicado = models.BooleanField(default=False)
    photo_image = models.ImageField('Trabalho', upload_to='portfolio/portfolio_image/%d/%m/%Y/',
                                    blank=True, default='')
    category = models.ForeignKey( 
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None, verbose_name=_('Categoria'),
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name=_('Autor'),
    )

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('portfolio:photos-photo', args=(self.id,))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.titulo)}'
            self.slug = slug

        return super().save(*args, **kwargs)
    
    def clean(self, *args, **kwargs):
        error_message = defaultdict(list)
        DB_photos = Photos.objects.filter(
            titulo__iexact = self.titulo
        ). first()

        if DB_photos:
            if DB_photos.pk != self.pk:
                error_message['titulo'].append(
                    'Esse título já está sendo usado!!!'
                )

            if error_message:
                raise ValidationError(error_message)
            
    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')