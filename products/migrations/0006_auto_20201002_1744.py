# Generated by Django 3.1 on 2020-10-02 14:44

import datetime
from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201002_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайдер', 'verbose_name_plural': 'Слайдеры'},
        ),
        migrations.AddField(
            model_name='slider',
            name='add_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 471922), verbose_name='Время добавления'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(default='', upload_to='images', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='slider',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('ACC', 'Accessory'), ('LQD', 'Liquid')], max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default='err', max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 469897), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('IS', 'Испарители'), ('CRT', 'Картриджи'), ('MND', 'Мундштуки'), ('NMK', 'Намотки'), ('VTA', 'Вата')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='crate',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 469897), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 469897), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='newproduct',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 471922), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 2, 17, 44, 6, 472889), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
