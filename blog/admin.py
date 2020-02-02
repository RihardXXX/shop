from django.contrib import admin
from .models import *

"""Тут прописываем, как будет работать наша админ панель нашего приложения"""



"""Импортируем и подключаем файл с управлением адм части постов"""
from .post_admin import PostAdmin


"""Импортируем и подключаем файл с управлением адм части категорий"""
from .category_admin import CategoryAdmin




admin.site.register(Comment)
admin.site.register(Tag)


#====================================================================================================================
# Шпаргалка по выведению и администрированию модели в админ части фреймворка, офиц документация

# from django.contrib import admin
# from myapp.models import Article
#
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
# make_published.short_description = "Mark selected stories as published"
#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published]

# admin.site.register(Article, ArticleAdmin)
#===================================================================================================================



