# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewRebalance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.TextField()),
                ('name', models.CharField(default=b'', max_length=200)),
                ('action', models.TextField()),
                ('adjustCash', models.BooleanField(default=False)),
                ('adjustWeightDuringRebal', models.BooleanField(default=False)),
                ('excludePendingTrades', models.BooleanField(default=False)),
                ('reviewSwapSale', models.BooleanField(default=False)),
                ('adjustCashDuringRebal', models.BooleanField(default=False)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('taxLotAlgo', models.CharField(default=b'FIFO', max_length=80,
                                                choices=[(b'FIFO', b'FIFO'), (b'LIFO', b'LIFO'),
                                                         (b'AVGCOST', b'Average Cost')])),
            ],
            options={
                'ordering': ('createDate',),
            },
        ),
    ]
