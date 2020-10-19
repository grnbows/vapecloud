# Generated by Django 3.1 on 2020-10-18 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20201018_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('vata', 'Вата'), ('isparitel', 'Испарители'), ('mundshtuki', 'Мундштуки'), ('namotki', 'Намотки'), ('kartridzh', 'Картриджи')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], max_length=255, null=True, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 59, 4, 849561), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 59, 4, 845173), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 18, 22, 59, 4, 848751), verbose_name='Время добавления'),
        ),
    ]
