# Generated by Django 3.1 on 2020-10-18 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20201018_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('mundshtuki', 'Мундштуки'), ('kartridzh', 'Картриджи'), ('vata', 'Вата'), ('namotki', 'Намотки'), ('isparitel', 'Испарители')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('YES', 'Да'), ('NO', 'Нет')], max_length=255, null=True, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 33, 49, 366733), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 33, 49, 362059), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 33, 49, 365872), verbose_name='Время добавления'),
        ),
    ]
