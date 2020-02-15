from django.db import models  # Из модуля импортируем модели
from django.contrib.auth.models import User
from django.utils import timezone
from mptt.models import MPTTModel # библиотека для работы с подкатегориями
from mptt.fields import TreeForeignKey
from django.urls import reverse
"""
        Тут описывается, как должны выглядеть наши таблицы в базе данных
        ====================================================================
        Свойства, которое описано в классе будут столбцами в таблицах базы данных
        """


class Category(MPTTModel):
    """Модель категорий"""
    """из модуля находим класс и наследуемся от него"""
    """создаем свойство класса, который создаст столбец таблицы в БД для имени и url"""
    name = models.CharField(verbose_name="имя", max_length=140)
    slug = models.SlugField(verbose_name="url", max_length=100)
    description = models.TextField(verbose_name='описание', max_length=1000, default="", blank=True)
    """Создаем подкатегорию, например внутри основной категории"""
    parent = TreeForeignKey(
        'self',
        verbose_name='родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    template = models.CharField(verbose_name="шаблон", max_length=500, default="blog/post_list.html")
    published = models.BooleanField(verbose_name="отображать", default=True)
    paginated = models.PositiveIntegerField(verbose_name="количество статей на странице", default=5)
    sort = models.PositiveIntegerField(verbose_name="порядок", default=0)

    def get_id_category(self):
        return self.id

    def __str__(self):
        """Прописываем метод, чтобы в админ панели выводилось распечатку объекта"""
        return self.name

    class Meta:
        """Этот метод меняет название класса в админ части сайта"""
        verbose_name = 'Категория'
        """название класса в множественном числе"""
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ("sort", ) # порядок сортировки категорий


class Tag(models.Model):
    """Модель Тэгов"""
    name = models.CharField(verbose_name="имя", max_length=140)
    slug = models.SlugField(verbose_name="url", max_length=100)
    published = models.BooleanField(verbose_name="отображать?", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def get_absolute_url(self):
        return reverse('detail_tag', kwargs={'tags': self.name, 'slug': self.slug})


class Post(models.Model):
    """Модель Постов"""
    title = models.CharField(verbose_name="Заглавие", max_length=500)
    mini_text = models.TextField(verbose_name="краткое содержание")
    text = models.TextField(verbose_name='полное содержание', max_length=10000000)
    created_date = models.DateField(verbose_name='дата создания', auto_now_add=True)
    slug = models.SlugField(verbose_name='url', max_length=100, unique=True)
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='тэг', blank=True)
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.SET_NULL, null=True, blank=True)
    subtitle = models.CharField(verbose_name="подзаголовок", max_length=500, blank=True, null=True)
    published_date = models.DateTimeField(
        verbose_name="дата публикации",
        default=timezone.now,
        blank=True,
        null=True
    )
    edit_date = models.DateTimeField(
        verbose_name="дата редактирования",
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField(verbose_name="главная фотография", upload_to="post/", null=True, blank=True)
    template = models.CharField(verbose_name="шаблон", max_length=500, default="blog/detail_post.html")
    published = models.BooleanField(verbose_name="опубликовать?", default=True)
    viewed = models.PositiveIntegerField(verbose_name="просмотрено", default=0)
    status = models.BooleanField(verbose_name="для зарегистрированных", default=False)
    sort = models.PositiveIntegerField(verbose_name="порядок", default=0)

    def __str__(self):
        return "{}".format(self.title)

    def get_tags(self):
        return self.tags.all()

    def get_comment_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

    def get_category_template(self):
        return self.category.template
    # def get_all_comments(self):
    #     pass

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ["sort", "-published_date"] # сортировка новостей по дате публикации новые наверху


class Comment(models.Model):
    """Модель комментариев"""
    post = models.ForeignKey(
        Post,
        verbose_name='статья',
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(verbose_name='текст комментария')
    created_date = models.DateField('дата создания', auto_now=True)
    moderation = models.BooleanField(default=False)
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
