# Generated by Django 3.0.8 on 2020-08-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_post',
            field=models.ImageField(upload_to='img', verbose_name='Изображение'),
        ),
    ]
