from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    "Создаем визуализацию для комментариев"
    list_display = ['text', 'created_date', 'moderation', 'author']
    list_display_links = ('author', )
    list_filter = ('author',)
    actions = ['make_published_false', 'make_published_true']

    def get_message_change(self, number_change):                                   # сообщение которое возвращаем в зависимости
        if number_change == 1:                                                     # от количества изменений изменяем цифру
            message_bit = "1 одно изменение произошло"
        else:
            message_bit = "%s изменний произошло" % number_change
        return message_bit                                                         # возвращаемая строка о количестве изменений

    def make_published_false(self, request, queryset):
        count = queryset.update(moderation=False)                                   # переключение публикации в отключить
        message = self.get_message_change(count)                                   # вызов метода возвращающая строку в зависимости от количества изменений
        self.message_user(request, message)                                        # ответ после внесенных изменений


    def make_published_true(self, request, queryset):
        count = queryset.update(moderation=True)                                    # переключение публикации в отключить
        message = self.get_message_change(count)                                   # вызов метода возвращающая строку в зависимости от количества изменений
        self.message_user(request, message)                                        # ответ после внесенных изменений

    make_published_false.short_description = "Снять с публикации комментарий"      # как будет метод выглядеть в админ панели
    make_published_true.short_description = "Опубликовать комментарий"             # как будет метод выглядеть в админ панели





admin.site.register(Comment, CommentAdmin)