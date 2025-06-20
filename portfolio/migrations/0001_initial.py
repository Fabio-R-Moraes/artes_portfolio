# Generated by Django 5.2.1 on 2025-06-04 22:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=65)),
                ('descricao', models.CharField(max_length=165)),
                ('slug', models.SlugField()),
                ('historia', models.TextField()),
                ('historia_html', models.BooleanField(default=False)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('esta_publicado', models.BooleanField(default=False)),
                ('photo_image', models.ImageField(upload_to='portfolio/portfolio_image/%d/%m/%Y')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.category')),
            ],
        ),
    ]
