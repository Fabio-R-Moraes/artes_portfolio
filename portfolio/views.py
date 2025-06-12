from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Photos
from django.http import Http404
from django.db.models import Q
from utils.pagination import make_pagination
import os

PER_PAGE = os.environ.get('PHOTOS_PER_PAGE',6)

def home(request):
    photos = get_list_or_404(Photos.objects.filter(
        esta_publicado=True
        ).order_by('-id'))
    
    pagina_objeto, range_paginacao = make_pagination(request, photos, PER_PAGE)
    return render(request, 'pages/home.html', context={
        'photos': pagina_objeto,
        'range_paginacao': range_paginacao,
    })

def category(request, category_id):
    photos = get_list_or_404(Photos.objects.filter(
        category__id=category_id, 
        esta_publicado=True
        ).order_by('-id'))
    pagina_objeto, range_paginacao = make_pagination(request, photos, PER_PAGE)
    return render(request, 'pages/category.html', context={
        'photos': pagina_objeto,
        'range_paginacao': range_paginacao,
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

def search(request):
    termo_procurado = request.GET.get('q','').strip()

    if not termo_procurado:
        raise Http404
    
    photo = Photos.objects.filter(
        Q(
            Q(titulo__icontains=termo_procurado)|
            Q(descricao__icontains=termo_procurado),
        ),
        esta_publicado=True,
    ).order_by('-titulo')
    pagina_objeto, range_paginacao = make_pagination(request, photo, PER_PAGE)
    return render(request, 'pages/search.html', context={
        'page_title': f' Pesquisando por "{termo_procurado}" |',
        'photos': pagina_objeto,
        'range_paginacao': range_paginacao,
        'aditional_url_query':f'&q={termo_procurado}',
    })
