# Generated by Django 3.2.4 on 2022-07-25 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_series_list_hide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series_shares',
            name='photo',
        ),
    ]