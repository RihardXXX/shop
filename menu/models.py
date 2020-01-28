from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

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

    def items(self):
        return self.menuitem_set.all()
    

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

    # content_type = models.ForeignKey(
    #     ContentType,
    #     verbose_name="Ссылка на",
    #     limit_choices_to=settings.MENU_APPS,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True)
    # object_id = models.PositiveIntegerField('Id записи', default=1, null=True)
    # content_object = GenericForeignKey('content_type', 'object_id')
    # sort = models.PositiveIntegerField('Порядок', default=0)
    # published = models.BooleanField("Отображать?", default=True)

    
    def __str__(self):
        return self.name

    def get_anchor(self):
        if self.anchor:
            return "{}/#{}".format(Site.objects.get_current().domain, self.anchor)
        else:
            return False
    

    
    
    
