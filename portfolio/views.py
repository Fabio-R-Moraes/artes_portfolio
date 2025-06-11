from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Photos

def home(request):
    photos = get_list_or_404(Photos.objects.filter(
        esta_publicado=True
        ).order_by('-id'))
    return render(request, 'pages/home.html', context={
        'photos': photos,
    })

def category(request, category_id):
    photos = get_list_or_404(Photos.objects.filter(
        category__id=category_id, 
        esta_publicado=True
        ).order_by('-id'))
    return render(request, 'pages/category.html', context={
        'photos': photos,
        'title': f'{photos[0].category.nome} - Categoria | ',
    })

def photo(request, id):
    photo = get_object_or_404(Photos,
        pk=id,
        esta_publicado=True,
    )
    return render(request, 'pages/photo-view.html', context={
        'photo': photo,
        'is_detail_page': True,
    })
