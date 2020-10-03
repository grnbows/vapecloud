# Generated by Django 3.1 on 2020-10-03 08:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201003_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='accessory',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 11, 51, 7, 765377), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='type_category',
            field=models.CharField(choices=[('NMK', 'Намотки'), ('MND', 'Мундштуки'), ('IS', 'Испарители'), ('CRT', 'Картриджи'), ('VTA', 'Вата')], max_length=255, null=True, verbose_name='Подтверди название категории'),
        ),
        migrations.AlterField(
            model_name='crate',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 11, 51, 7, 765377), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 11, 51, 7, 765377), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='salt',
            field=models.CharField(choices=[('NO', 'Нет'), ('YES', 'Да')], max_length=255, verbose_name='SALT'),
        ),
        migrations.AlterField(
            model_name='order',
            name='event_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 11, 51, 7, 768370), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='add_time',
            field=models.TimeField(default=datetime.datetime(2020, 10, 3, 11, 51, 7, 767372), verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='table',
            field=models.CharField(choices=[('Accessory', 'Accessory'), ('Liquid', 'Liquid')], max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='Наименование'),
        ),
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('producted_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.producted')),
                ('memory_size', models.CharField(max_length=20)),
                ('storage_size', models.CharField(max_length=20)),
            ],
            bases=('products.producted',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('producted_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.producted')),
                ('resolution', models.CharField(max_length=20)),
                ('screen_size', models.CharField(max_length=20)),
            ],
            bases=('products.producted',),
        ),
    ]