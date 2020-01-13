from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  .models import *

"""тут описываем логику работы программы при получении запроса"""

class HomeVew(View):
    """Наследуемся от класса view"""

    def get(self, request):
        """Описываем что будет делать метод get"""
        post_list = Post.objects.all()
        return render(request, 'blog/home.html', {"posts": post_list})

    def post(self, request):
        """описываем что будет делать метод post"""
        pass


class CategoryView(View):
    """Вывод статей по категориям"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {"category": category})