from django.db import models #                                      Из модуля импортируем модели

"""
Тут описывается, как должны выглядеть наши таблицы в базе данных
====================================================================
Свойства, которое описано в классе будут столбцами в таблицах базы данных
"""

class Category(models.Model):
    """Модель категорий"""
    """из модуля находим класс и наследуемся от него"""
    """создаем свойство класса, который создаст столбец таблицы в БД для имени и url"""
    name = models.CharField(verbose_name="имя", max_length=140)
    slug = models.SlugField(verbose_name="url", max_length=100)

    def __str__(self):
        """Прописываем метод, чтобы в админ панели выводилось распечатку объекта"""
        return self.name

    class Meta:
        """Этот метод меняет название класса в админ части сайта"""
        verbose_name = 'Категория'
        """название класса в множественном числе"""
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Модель Тэгов"""
    name = models.CharField(verbose_name="имя", max_length=140)
    slug = models.SlugField(verbose_name="url", max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        
        
class Post(models.Model):
    """Модель Постов"""
    title = models.CharField(verbose_name="Заглавие", max_length=140)
    mini_text = models.TextField(verbose_name="обзор статьи")
    text = models.TextField(verbose_name='текст статьи')
    created_date = models.DateField()
    slug = models.SlugField(verbose_name='url', max_length=100)
    
    def __str__(self):
        return self
    
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
        
        
class Comment(models.Model):
    """Модель комментариев"""
    text = models.TextField(verbose_name='текст комментария')
    created_date = models.DateField()
    moderation = models.BooleanField()
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural='Комментарии'
        