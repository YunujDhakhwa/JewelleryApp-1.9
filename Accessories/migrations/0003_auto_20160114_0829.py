# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accessories', '0002_auto_20151226_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='date',
        ),
        migrations.RemoveField(
            model_name='material',
            name='material_id',
        ),
        migrations.RemoveField(
            model_name='material',
            name='material_name',
        ),
        migrations.RemoveField(
            model_name='material',
            name='price',
        ),
        migrations.AddField(
            model_name='material',
            name='goldPrice',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='materialDate',
            field=models.CharField(default=b'2016-01-14', max_length=15, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='material',
            name='silverPrice',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]