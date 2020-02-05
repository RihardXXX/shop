from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

from blog.models import Post


def get_home_page(request):
    # return HttpResponse("start")
    template = 'blog/post_list.html'  # шаблон по умолчанию
    posts = Post.objects.filter(published_date__lte=datetime.now(), published=True)
    return render(request, template, {
        "posts": posts
    })
