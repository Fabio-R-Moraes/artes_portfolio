from django.shortcuts import render
from utils.fabrica import make_photo

def home(request):
    return render(request, 'pages/home.html', context={
        'photos':[make_photo() for _ in range(10)],
    })

def photo(request, id):
    return render(request, 'pages/photo-view.html', context={
        'photo': make_photo(),
    })
