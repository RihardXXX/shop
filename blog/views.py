from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from  .models import *
from .forms import CommentForm

"""тут описываем логику работы программы при получении запроса"""


# all_posts = Post.objects.filter(published_date__lte=datetime.now(), published=True)  # берем все посты с базы
# paginator = Paginator(all_posts, 8)  # создаем объект пагинатор, чтобы на 1 стр 4 поста было
# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)
# return render(request, template, {
#     'page_obj': page_obj,
#     "tags": tags
# })


class PostListView(View):
    """Вывод статей по категориям, тэгам, домашняя страница"""

    def my_paginator(self,request, all_posts, number_posts=8):
        paginator = Paginator(all_posts, number_posts)  # создаем объект пагинатор, чтобы на 1 стр 4 поста было
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, slug=None):
        """Очень умный орм запрос, получаемый объект куери сет объект постов мы ставим фильтр,
        чтобы слаг категории внутри объекта поста совпадал со слагом с маршрута юрл"""
        """Два подчеркивания это обращение"""
        tags = Tag.objects.all()
        template = 'blog/index.html' # шаблон по умолчанию
        if category_slug is not None: # если в запрос пришло название категории
            all_posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)# сортировка по категориям
            page_obj = self.my_paginator(request, all_posts)
        elif slug is not None: # если в запрос пришло название тэга
            all_posts = self.get_queryset().filter(tags__slug=slug)  # сортировка по тегам
            page_obj = self.my_paginator(request, all_posts)
        # return render(request, template, {"posts": posts, "tags" : tags })
        return render(request, template, {
            'page_obj': page_obj,
            "tags": tags
        })



class PostDetailView(View):
    """Класс открывающий всю статью"""

    def get(self, request, **kwargs):
        """Описываем что будет делать метод get"""
        #category_list = Category.objects.all()
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        tags = Tag.objects.all()
        form = CommentForm()
        return render(request, post.template,
                      {"categories": category_list,
                       "post": post,
                       "form": form,
                       "tags": tags}
        )
        # post = get_object_or_404(Post, slug=kwargs.get("slug")) # вернуть 404 если страницы не совпадают
        # comment = Comment.objects.filter(post_id=post.id) # комменты привязанные к этой статье
        # form = CommentForm()
        # return render(request, post.template, {
        #     "post": post,
        #     "comments": comment,
        #     "form": form
        # })

    def post(self, request, **kwargs):
        # Comment.objects.create( # первый метод создания объекта для записи в базу данных
        #     author=request.user,
        #     post_id=request.POST.get("post"),
        #     text=request.POST.get("text")
        # )
        # comment = Comment() # второй способ записи данных  в базу данных
        # comment.author = request.user
        # comment.post_id = request.POST.get("post")
        # comment.text = request.POST.get("text")
        # comment.save()
        print(request.POST)
        print(kwargs)
        form = CommentForm(request.POST) # создается объект с заполненными даными для БД
        if form.is_valid(): # если отправленные данные валидны
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get("slug"))
            form.author = request.user
            form.save()
        return redirect(request.path)

