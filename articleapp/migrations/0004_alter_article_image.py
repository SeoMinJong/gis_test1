# Generated by Django 3.2.4 on 2021-08-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0003_article_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='article/'),
        ),
    ]
