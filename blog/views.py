from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from  .models import *

"""тут описываем логику работы программы при получении запроса"""


class PostListView(View):
    """Вывод статей по категориям, тэгам, домашняя страница"""

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_name=None, slug=None):
        """Очень умный орм запрос, получаемый объект куери сет объект постов мы ставим фильтр,
        чтобы слаг категории внутри объекта поста совпадал со слагом с маршрута юрл"""
        """Два подчеркивания это обращение"""
        category_list = Category.objects.all() # полный список категорий
        template = 'blog/post_list.html' # шаблон по умолчанию
        if category_name is not None: # если в запрос пришло название категории
            posts = self.get_queryset().filter(category__slug=category_name, category__published=True)# сортировка по категориям
        elif slug is not None: # если в запрос пришло название тэга
            posts = self.get_queryset().filter(tags__slug=slug)  # сортировка по тегам
        else: # если ничего не пришло
            posts = self.get_queryset()  # полный список статей
        return render(request, template, {"posts": posts, "categories": category_list})



class PostDetailView(View):
    """Класс открывающий всю статью"""

    def get(self, request, **kwargs):
        """Описываем что будет делать метод get"""
        category_list = Category.objects.all()
        post = get_object_or_404(Post, slug=kwargs.get("slug")) # вернуть 404 если страницы не совпадают
        comment = Comment.objects.filter(post_id=post.id)
        return render(request, post.template, {
            "post": post,
            "categories": category_list,
            "comments": comment
        })