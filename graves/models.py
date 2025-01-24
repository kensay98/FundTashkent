from django.db import models
from django_summernote.fields import SummernoteTextField
import requests
from datetime import datetime

GRAVES_CHOICES = [
    (1, 'Текстиль'),
    (2, 'Чигатай')
]


class Graves(models.Model):
    class Meta:
        verbose_name = 'Могила'
        verbose_name_plural = 'Могилы'


    def generate_path():
        return "%s/%s/" % (datetime.now().year, datetime.now().month)
    
    name = models.CharField(max_length=200, verbose_name='Имя')
    birthday = models.CharField(verbose_name='Дата рождения', max_length=128)
    day_of_death = models.CharField(verbose_name='Дата смерти', max_length=128)
    sector = models.CharField(max_length=200, verbose_name='Карта')
    row = models.CharField(max_length=200, verbose_name='Ряд')
    number = models.CharField(max_length=200, verbose_name='Номер')
    part_ww = models.IntegerField(verbose_name='Учавствовал ли во ВоВ?')
    photo = models.FileField(verbose_name='Фото')
    big_photo = models.FileField(verbose_name='Фото', upload_to='%Y/%m/')
    cemetery = models.IntegerField(verbose_name='Кладбище', choices=GRAVES_CHOICES)

    def __str__(self):
        return self.name

    def have_photo(self):
        try:
            response = requests.request("GET", "http://fundtashkent.org/%s" % self.big_photo.url)
            if(response.status_code == 200):
                return True
            elif(response.status_code == 404):
                return False
        except:
            return False


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(verbose_name='Дата и время')

    def __str__(self):
        return self.title


class Page(models.Model):
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    name = models.CharField(max_length=200, verbose_name='Название')
    text = SummernoteTextField(verbose_name='Содержимое')

    def __str__(self):
        return self.name


class OurProjects(models.Model):
    class Meta:
        verbose_name = 'Наш проект'
        verbose_name_plural = 'Наши проекты'

    title = models.CharField(verbose_name='Закоголовок', max_length=200)
    before_photo = models.ImageField(verbose_name='Фото До')
    after_photo = models.ImageField(verbose_name='Фото После')
    description = models.TextField(verbose_name='Описание')


class Memorials(models.Model):
    class Meta:
        verbose_name = 'Памятник'
        verbose_name_plural = 'Памятники'

    number = models.IntegerField(verbose_name='Номер могилы')
    photo = models.CharField(max_length=100, verbose_name='Фото')
    translation = models.TextField(verbose_name='Перевод')

    def __str__(self):
        return self.photo
