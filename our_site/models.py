from django.db import models
from datetime import date


class Legend_IVT(models.Model):
    name = models.CharField('Имя легенды', max_length=200)
    surname = models.CharField('Фамилия легенды', max_length=200)
    nickname = models.CharField('прозвище легенды', max_length=200, blank=True)
    date_of_born = models.DateField('Дата рождения легенды')
    description = models.TextField('Описание легенды')
    photo = models.ImageField('Фотография легенды', upload_to="photo_of_legend/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Легенда ИВТ'
        verbose_name_plural = 'Легенды ИВТ'


class Photo(models.Model):
    name = models.CharField('Название фото', max_length=200, blank=True)
    description = models.TextField('Описание фотографии', blank=True)
    img = models.ImageField(upload_to="photos/")
    date_of_post = models.DateTimeField('Дата публикации фото', auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Legend_on_photo(models.Model):
    legend = models.ForeignKey(Legend_IVT, verbose_name='Легенда', on_delete=models.SET_NULL, null=True)
    photo = models.ForeignKey(Photo, verbose_name='Фото', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Легенда на фотографии'
        verbose_name_plural = 'Легенды на фотографии'


class Comments(models.Model):
    photo = models.ForeignKey(Photo, verbose_name='Фотография', on_delete=models.CASCADE)
    date_of_comment = models.DateField('Дата публикации комментария', default=date.today)
    name_of_commentor = models.CharField('Имя комментатора', max_length=200)
    text_of_comment = models.TextField('Текст комментария', max_length=5000)

    def __str__(self):
        return f"{self.name_of_commentor}-{self.news}"

    class Meta:
        verbose_name = 'Коментарий к посту'
        verbose_name_plural = 'Комментарии к посту'
