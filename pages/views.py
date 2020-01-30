from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.views import View

from .models import Page



class AboutView(View):

    @csrf_protect
    def render_page(request, page):
        """Рендер страницы"""
        if page.registration_required and not request.user.is_authenticated:
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.path)
        return render(request, page.template, {"page": page})

    def get_page(request, url):
        """Получение страницы по url"""
        if not url.startswith('/'):
            url = '/' + url
        try:
            page = get_object_or_404(Page, slug=url, published=True)
        except Http404:
            if not url.endswith('/') and settings.APPEND_SLASH:
                url += '/'
                page = get_object_or_404(Page, slug=url, published=True)
                return HttpResponsePermanentRedirect('%s/' % request.path)
            else:
                raise

        return AboutView.render_page(request, page)


    # def get(self, request, url):
    #     page = Page.objects.all()
    #     template = 'pages/home.html'
    #     return render(request, template, {
    #         "page" : page,
    #     })
