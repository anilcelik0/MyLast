# Generated by Django 3.2.4 on 2022-07-19 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0008_auto_20220715_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_list_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='book_list_content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='book.books')),
                ('book_list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_list_name', to='book.book_list')),
            ],
        ),
    ]