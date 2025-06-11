from django.contrib import admin
from .models import Category, Photos

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug')