"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # подключаю виджет уже пол дня))) это жесть
    path('accounts/', include('allauth.urls')),            # регистрируем путь для приложения авторизации
    path('blog/', include("blog.urls")),                   # подключение приложение блог
    path('page/', include("pages.urls")),                  # подключаем приложение pages
    path('feedback/', include("feedback.urls")),           # подключаем приложение feedback
    path('', include("home.urls")),                        # подключаем приложение домашняя страница
]

"""Корневой файл всех запросов, который сортирует все запросы по категориям запросов"""

"""Медиа папку подключаем в корне"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)