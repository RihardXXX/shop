from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

from blog.models import Post
from blog.models import Tag


def get_home_page(request):
    # return HttpResponse("start")
    template = 'blog/index.html'  # шаблон по умолчанию
    posts = Post.objects.filter(published_date__lte=datetime.now(), published=True)
    tags = Tag.objects.all()
    return render(request, template, {
        "posts": posts,
        "tags": tags
    })
