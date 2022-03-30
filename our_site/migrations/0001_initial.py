# Generated by Django 3.2.3 on 2022-03-30 19:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legend_IVT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя легенды')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия легенды')),
                ('nickname', models.CharField(blank=True, max_length=200, verbose_name='прозвище легенды')),
                ('date_of_born', models.DateField(verbose_name='Дата рождения легенды')),
                ('description', models.TextField(verbose_name='Описание легенды')),
                ('photo', models.ImageField(upload_to='photo_of_legend/', verbose_name='Фотография легенды')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название фото')),
                ('description', models.TextField(blank=True, verbose_name='Описание фотографии')),
                ('img', models.ImageField(upload_to='photos/')),
                ('date_of_post', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации фото')),
            ],
        ),
        migrations.CreateModel(
            name='Legend_on_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legend', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='our_site.legend_ivt', verbose_name='Легенда')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='our_site.photo', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_comment', models.DateField(default=datetime.date.today, verbose_name='Дата публикации комментария')),
                ('name_of_commentor', models.CharField(max_length=200, verbose_name='Имя комментатора')),
                ('text_of_comment', models.TextField(max_length=5000, verbose_name='Текст комментария')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_site.photo', verbose_name='Фотография')),
            ],
        ),
    ]
