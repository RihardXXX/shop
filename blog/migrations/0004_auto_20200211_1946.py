# Generated by Django 2.2.9 on 2020-02-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200128_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
    ]