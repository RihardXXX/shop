from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  .models import *

"""тут описываем логику работы программы при получении запроса"""

class HomeVew(View):
    """Наследуемся от класса view"""

    def get(self, request):
        """Описываем что будет делать метод get"""
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {
            "posts": post_list,
            "categories": category_list
        })

    def post(self, request):
        """описываем что будет делать метод post"""
        pass


class PostDetailView(View):
    """Класс открывающий всю статью"""
    def get(self, request, category, slug):
        """Описываем что будет делать метод get"""
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        # tags = post.get_tags()
        # print(tags)
        comment = Comment.objects.filter(post_id=post.id)
        return render(request, post.template, {
            "post": post,
            "categories": category_list,
            "comments": comment
        })


class CategoryView(View):
    """Вывод статей по категориям"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {"category": category})