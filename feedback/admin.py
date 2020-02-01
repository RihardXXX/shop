from django.contrib import admin
"""Тут прописываем, как будет работать наша админ панель нашего приложения"""

"""Импортируем Класс Категори из файла модели"""
from .models import Feedback





"""Регистрируем наш класс модель для управления в админ части сайта"""
admin.site.register(Feedback)
