from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.core.paginator import Paginator
from blog.models import Post
from blog.models import Tag




def get_home_page(request):
    # return HttpResponse("start")
    template = 'blog/index.html'                                                        # шаблон по умолчанию
    all_posts = Post.objects.filter(published_date__lte=datetime.now(), published=True) # берем все посты с базы
    paginator = Paginator(all_posts, 8)                              # создаем объект пагинатор, чтобы на 1 стр 4 поста было
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    return render(request, template, {
        'page_obj': page_obj,
        "tags": tags
    })

#   Шпаргалка по пагинатору с официальной документации
# def listing(request):
#     contact_list = Contact.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page.
#
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'list.html', {'page_obj': page_obj})