from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome =  models.CharField(max_length=65)

    def __str__(self):
        return self.nome

class Photos(models.Model):
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    historia = models.TextField()
    historia_html = models.BooleanField(default=False)
    preco = models.DecimalField(decimal_places=2, max_digits=9)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    esta_publicado = models.BooleanField(default=False)
    photo_image = models.ImageField(upload_to='portfolio/portfolio_image/%d/%m/%Y/',
                                    blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
    )

    def __str__(self):
        return self.titulo