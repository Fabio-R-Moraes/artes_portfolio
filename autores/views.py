from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404
from django.contrib import messages
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from portfolio.models import Photos
from autores.forms.photo_form import AuthorsPhotoForm

def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(request, 'pages/register_view.html', context={
        'form': form,
        'form_action': reverse('autores:register_create')
    })

def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.set_password(usuario.password)
        usuario.save()
        messages.success(request, 'Seu usuário foi criado, por favor, faça o login...')
        del(request.session['register_form_data'])

    return redirect('autores:login')

def login_view(request):
    form = LoginForm()

    return render(request, 'pages/login.html', context={
        'form': form, 
        'form_action': reverse('autores:login_create')
    })

def login_create(request):

    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)
    login_url = reverse('autores:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado!!!')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais Inválidas...')
    else:
        messages.errorq(request, 'Usuário ou senha inválidos!!!')

    return redirect(reverse('autores:dashboard'))

@login_required(login_url='autores:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('autores:login'))
    
    if request.POST.get('username')!=request.user.username:
        return redirect(reverse('autores:login'))
    
    logout(request)
    return redirect(reverse('autores:login'))
    
@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard(request):
    my_photos = Photos.objects.filter(
        esta_publicado = False,
        author = request.user
    )
    return render(request, 'pages/dashboard.html', context={
        'photos': my_photos,
    })

@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard_photo_edit(request, id):
    my_photo = Photos.objects.filter(
        esta_publicado = False,
        author = request.user,
        pk = id
    ).first()

    if not my_photo:
        raise Http404()

    formulary = AuthorsPhotoForm(
        data = request.POST or None,
        files = request.FILES or None, 
        instance=my_photo
    )

    if formulary.is_valid():
        photo = formulary.save(commit=False)
        photo.author = request.user
        photo.historia_html = False
        photo.esta_publicado = False

        photo.save()
        messages.success(request, 'Seu trabalho foi salvo com sucesso!!!')
        return redirect(reverse('autores:dashboard_photo_edit', args=(id,)))

    return render(request, 'pages/dashboard_photos.html', context={
        'form': formulary,
    })

@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard_photo_new(request):
    formulary = AuthorsPhotoForm(
        data = request.POST or None,
        files = request.FILES or None,
    )

    if formulary.is_valid():
        photo:Photos = formulary.save(commit=False)
        photo.author = request.user
        photo.historia_html = False
        photo.esta_publicado = False

        photo.save()
        messages.success(request, 'Seu trabalho foi salvo com sucesso!!!')
        return redirect(reverse('autores:dashboard_photo_edit', args=(photo.id,)))
    
    return render(request, 'pages/dashboard_photos.html', context={
        'form': formulary,
        'form_action': reverse('autores:dashboard_photo_new'),
    })

@login_required(login_url='autores:login', redirect_field_name='next')
def dashboard_photo_delete(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    id = POST.get('id')
    
    my_photo = Photos.objects.filter(
        esta_publicado = False,
        author = request.user,
        pk = id,
    ).first()

    if not my_photo:
        raise Http404()
    
    my_photo.delete()
    messages.success(request, 'Seu trabalho foi excluído com sucesso!!!')

    return redirect(reverse('autores:dashboard'))