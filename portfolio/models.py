from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    nome =  models.CharField('Categoria', max_length=65)

    def __str__(self):
        return self.nome

class Photos(models.Model):
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
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
    )
    #tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('portfolio:photos-photo', args=(self.id,))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.titulo)}'
            self.slug = slug

        return super().save(*args, **kwargs)