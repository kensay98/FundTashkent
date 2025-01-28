# Generated by Django 4.2.18 on 2025-01-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graves', '0009_alter_graves_big_photo_alter_graves_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='graves',
            name='first_name',
            field=models.CharField(default='', max_length=200, verbose_name='Имя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graves',
            name='last_name',
            field=models.CharField(default='', max_length=200, verbose_name='Фамилия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graves',
            name='third_name',
            field=models.CharField(default='', max_length=200, verbose_name='Отчество'),
            preserve_default=False,
        ),
    ]
