from django.contrib import admin
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PostAdmin(admin.ModelAdmin):
    """Создаем визуализацию в адм части нашей модели"""
    list_display = ['title', 'mini_text', 'author', 'published', 'category']       # пункты показываемые в адм панели джанго
    list_display_links = ('title',)                                                # указываем ссылкой какой пункт будет в админке
    list_filter = ('category',)                                                    # фильтро сортировки по категориям
    actions = ['make_published_false', 'make_published_true']                      # указываем какой экш должен работать в адм панели

    def get_message_change(self, number_change):                                   # сообщение которое возвращаем в зависимости
        if number_change == 1:                                                     # от количества изменений изменяем цифру
            message_bit = "1 одно изменение произошло"
        else:
            message_bit = "%s изменний произошло" % number_change
        return message_bit                                                         # возвращаемая строка о количестве изменений

    def make_published_false(self, request, queryset):
        count = queryset.update(published=False)                                   # переключение публикации в отключить
        message = self.get_message_change(count)                                   # вызов метода возвращающая строку в зависимости от количества изменений
        self.message_user(request, message)                                        # ответ после внесенных изменений


    def make_published_true(self, request, queryset):
        count = queryset.update(published=True)                                    # переключение публикации в отключить
        message = self.get_message_change(count)                                   # вызов метода возвращающая строку в зависимости от количества изменений
        self.message_user(request, message)                                        # ответ после внесенных изменений

    make_published_false.short_description = "Снять с публикации пост"             # как будет метод выглядеть в админ панели
    make_published_true.short_description = "Опубликовать пост"                    # как будет метод выглядеть в админ панели


admin.site.register(Post, PostAdmin)                                               # регистрируем класс визуализации в адм панели и показ в адм панели модели вообще