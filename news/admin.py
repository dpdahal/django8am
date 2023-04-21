from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image_tag', 'category', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'description']
    list_editable = ['is_published']

    def image_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />'.format(obj.photo.url))
        else:
            return 'No Image Found'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}