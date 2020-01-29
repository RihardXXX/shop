from django.shortcuts import render
from django.views import View
from .models import Page
from django.http import HttpResponse

class AboutView(View):

    def get(self, request, url):
        page = Page.objects.all()
        template = 'pages/home.html'
        return render(request, template, {
            "page" : page,
        })
