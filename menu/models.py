from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.conf import settings

class Menu(models.Model):
    """Позиция меню"""
    name  = models.CharField(verbose_name='название', max_length=200)
    is_auth = models.BooleanField(verbose_name="Для зарегистрированных или нет", default=False)
    activate = models.BooleanField(verbose_name='Вкл\Выкл', default=False)

    class Meta:
        """Прописываем название класса в административной части"""
        verbose_name='Меню'
        verbose_name_plural='менюшки'
        
    def __str__(self):
        return self.name
    

class MenuItem(MPTTModel):
    """Пукнты меню"""
    name = models.CharField(verbose_name='название латиницей', max_length=300)
    title = models.CharField(verbose_name='название меню', max_length=250)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родительский пункт",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name='меню', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name='Вкл\Выкл', default=False)
    is_auth = models.BooleanField(verbose_name='Для зарегистрированных или нет', default=False)
    anchor = models.CharField(verbose_name='якорь', max_length=255, null=True, blank=True)
    url = models.CharField(verbose_name='ссылка на внешний ресурс', max_length=300, null=True, blank=True)
    active = models.BooleanField(verbose_name='Вкл\Выкл', default=False)
    
    def __str__(self):
        return self.name
    

    
    
    
"""Задание:

5. Создать приложение Страницы
6. Создать модель Page
	1. title
	2. text
	3. active - Вкл\Выкл
	4. template - CharField - default='page/index.html'
	5. slug - url
7. Вывести страницы в админку
8. Доп. задание
	1. Написать view и url для вывода страниц

Доп. инфо:

Custom template tags - https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/

Django template tags - https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#for

Django request - https://docs.djangoproject.com/en/2.2/ref/request-response/

Репозиторий:

https://github.com/DJWOMS/CourseDjango2"""