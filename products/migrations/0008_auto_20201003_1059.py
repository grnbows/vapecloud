# Generated by Django 3.1 on 2020-10-03 07:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201002_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 10, 59, 50, 497281), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('CRT', 'Картриджи'), ('IS', 'Испарители'), ('NMK', 'Намотки'), ('MND', 'Мундштуки'), ('VTA', 'Вата')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='crate',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 10, 59, 50, 497281), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 10, 59, 50, 497281), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], max_length=255, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 10, 59, 50, 497281), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 10, 59, 50, 497281), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Liquid', 'Liquid'), ('Accessory', 'Accessory')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]
