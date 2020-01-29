# Generated by Django 2.2.9 on 2020-01-28 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200115_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['sort', '-published_date'], 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='статья'),
        ),
    ]