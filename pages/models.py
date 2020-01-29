from django.db import models

class Page(models.Model):
    """создаем таблицу страниц"""

    title = models.CharField(verbose_name="заголовок", max_length=355)
    text = models.TextField(verbose_name="текст страницы", null=True, blank=True)
    active = models.BooleanField(verbose_name="Вкл\Выкл", default=False)
    template = models.CharField(verbose_name="шаблон", max_length=500, default="pages/index.html")
    slug = models.SlugField(verbose_name="url", max_length=200, unique=True)

    def get_slug(self):
        return self.slug + self.slug

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = "/"
        if not f"{self.slug}".startswith("/"):
            self.slug = "/" + self.slug
        if not self.slug.endswith("/"):
            self.slug += "/"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        unique_together = ('slug',)







