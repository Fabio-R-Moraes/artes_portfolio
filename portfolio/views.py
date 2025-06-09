from django.shortcuts import render
from utils.fabrica import make_photo
from .models import Photos

def home(request):
    photos = Photos.objects.filter(esta_publicado=True).order_by('-id')
    return render(request, 'pages/home.html', context={
        'photos': photos,
    })

def category(request, category_id):
    photos = Photos.objects.filter(category__id=category_id, esta_publicado=True).order_by('-id')
    return render(request, 'pages/category.html', context={
        'photos': photos,
    })

def photo(request, id):
    return render(request, 'pages/photo-view.html', context={
        'photo': make_photo(),
        'is_detail_page': True,
    })
