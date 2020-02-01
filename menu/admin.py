from django.contrib import admin

# Register your models here.
from .models import *
from mptt.admin import MPTTModelAdmin




"""Тут пишем классы для визуализации и фильрации модели в админ части"""

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """визуализация меню"""
    list_display = ("name", "is_auth", "activate")                 # столбцы которые будут выводится в админ части
    list_filter = ("activate",)                                    # фильтр активировано или нет справа в админ части


@admin.register(MenuItem)                                          # декораторы которые запускаются в начале и регистрируют в адм. панели
class MenuItemAdmin(MPTTModelAdmin):
    """визуялизация пунктов меню в админ части"""
    list_display = ("name", "title", "parent", "menu", "sort", "object_id", "published")
    list_filter = ("menu", "parent", "published")
    search_fields = ("name", "parent__name", "menu__name")         # поиск в указанных параметрах
    save_as = True                                                 # появляется кнопка сохранить объект (клонирование)
    list_editable = ("sort",)
    mptt_level_indent = 20                                         # помогает отображать вложенность

