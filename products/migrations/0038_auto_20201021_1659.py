# Generated by Django 3.1 on 2020-10-21 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20201021_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('isparitel', 'Испарители'), ('namotki', 'Намотки'), ('vata', 'Вата'), ('mundshtuki', 'Мундштуки'), ('kartridzh', 'Картриджи')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 21, 16, 59, 34, 790468), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 21, 16, 59, 34, 785963), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 21, 16, 59, 34, 789664), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Cloud', 'Cloud'), ('Liquid', 'Liquid'), ('Others', 'Others'), ('Accessory', 'Accessory')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]
