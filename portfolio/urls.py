from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='photos-home'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('photo/<int:id>/', views.photo, name='photos-photo'),
    path('photo/search/', views.search, name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)