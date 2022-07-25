# Generated by Django 3.2.4 on 2022-07-20 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('series', '0003_alter_series_shares_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='series_list',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('yt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_list_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='series_list_content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('yt', models.DateTimeField(auto_now_add=True)),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='series.seriess')),
                ('series_list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_list_name', to='series.series_list')),
            ],
        ),
    ]
