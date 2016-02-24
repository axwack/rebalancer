# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0012_auto_20151103_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rebalanceName', models.CharField(max_length=100)),
                ('saleType', models.CharField(max_length=15)),
                ('buySell', models.CharField(max_length=5)),
                ('taxLots', models.CharField(max_length=100)),
            ],
        ),
    ]
