# Generated by Django 3.0.8 on 2020-08-15 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200816_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='article',
            new_name='article1',
        ),
    ]
