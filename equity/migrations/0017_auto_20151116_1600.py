# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0016_auto_20151111_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='RebalanceParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rebalanceName', models.CharField(unique=True, max_length=100)),
                ('saleType', models.CharField(max_length=15)),
                ('buySell', models.CharField(max_length=5)),
                ('reviewCurrentSale', models.BooleanField(default=False)),
                ('adjustCashAfterRebal', models.BooleanField(default=False)),
                ('adjustWgtAfterRebal', models.BooleanField(default=False)),
                ('taxLots', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='adjustCashAfterRebal',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='adjustWgtAfterRebal',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='buySell',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='rebalanceName',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='reviewCurrentSale',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='saleType',
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='taxLots',
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='accountsIncluded',
            field=models.ManyToManyField(to='equity.Account'),
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='acctFilterName',
            field=models.ForeignKey(default=7, to='equity.AccountFilters'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='excludeClassification',
            field=models.ForeignKey(default=0, to='equity.ClassificationNames'),
            preserve_default=False,
        ),
    ]
