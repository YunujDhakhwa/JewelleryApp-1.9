# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accessories', '0006_materialprice'),
        ('Product', '0007_remove_product_stone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stones',
            field=models.ManyToManyField(blank=True, null=True, to='Accessories.StoneType'),
        ),
    ]