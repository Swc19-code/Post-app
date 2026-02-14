from django.contrib import admin
from . models import Blog, Categories

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content', 'category', 'is_draft', 'author']


@admin.register(Categories)
class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'catName']