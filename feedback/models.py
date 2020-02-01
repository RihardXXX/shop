from django.db import models

class Feedback(models.Model):
    email = models.EmailField(verbose_name="почта", max_length=100)
    name = models.CharField(verbose_name="ФИО", max_length=200)
    text = models.TextField(verbose_name="текст сообщения", max_length=1000000)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="обратная связь"
        verbose_name_plural="Обратная связь"
        
    
