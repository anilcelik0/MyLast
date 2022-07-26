# Generated by Django 3.2.4 on 2022-07-26 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0012_remove_book_shares_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_saves',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('yt', models.DateTimeField(auto_now_add=True)),
                ('book_share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_share', to='book.book_shares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_share_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]