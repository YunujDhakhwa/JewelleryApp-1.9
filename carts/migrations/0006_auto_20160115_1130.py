# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_cartitem_itemprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='itemPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]