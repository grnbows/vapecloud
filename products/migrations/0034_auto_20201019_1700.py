# Generated by Django 3.1 on 2020-10-19 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20201019_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('namotki', 'Намотки'), ('kartridzh', 'Картриджи'), ('mundshtuki', 'Мундштуки'), ('vata', 'Вата'), ('isparitel', 'Испарители')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 0, 54, 87938), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 0, 54, 83150), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 19, 17, 0, 54, 87025), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Liquid', 'Liquid'), ('Accessory', 'Accessory')], max_length=255, null=True, verbose_name='Категория'),
        ),
    ]