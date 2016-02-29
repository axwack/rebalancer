# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acctCd',
                 models.CharField(default=b'ABC', max_length=200, unique=True, serialize=False, primary_key=True)),
                ('shortName', models.CharField(default=b'ABC', max_length=50)),
                ('cashSegregated', models.FloatField()),
                ('cashUnSegregated', models.FloatField()),
                ('totCash', models.FloatField()),
            ],
            options={
                'ordering': ('shortName',),
            },
        ),
        migrations.CreateModel(
            name='ClassificationNames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classificationName', models.CharField(max_length=100)),
                ('classificationLevel', models.IntegerField(),
                 # ('classificationLevel', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baseAcctCrncy', models.CharField(default=b'USD', max_length=5)),
                ('quantity', models.FloatField()),
                ('mktVal', models.FloatField()),
                ('pledgedQty', models.FloatField()),
                ('segQty', models.FloatField()),
                ('origCost', models.FloatField()),
                ('origFace', models.FloatField()),
                ('acctCd', models.ForeignKey(to='equity.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('secId', models.IntegerField(serialize=False, primary_key=True)),
                ('secName', models.CharField(max_length=100)),
                ('listExchCd', models.CharField(max_length=10)),
                ('baseCurrency', models.CharField(default=b'USD', max_length=5)),
                ('mktPrice', models.FloatField()),
                ('amtIssued', models.FloatField()),
                ('amtOutstanding', models.FloatField()),
                ('couponRate', models.FloatField()),
                ('identity', models.ForeignKey(to='equity.Identity')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityClassification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('classification', models.ForeignKey(to='equity.ClassificationNames')),
                ('secId', models.ForeignKey(to='equity.Security')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityType',
            fields=[
                ('secTypCd', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('secName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TaxLot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extTaxLotId', models.CharField(max_length=100)),
                ('tradeDate', models.DateField()),
                ('settleDate', models.DateField()),
                ('qty', models.FloatField()),
                ('costBaseAmount', models.FloatField()),
                ('incBaseAmount', models.FloatField()),
                ('unitBaseAmout', models.FloatField()),
                ('secId', models.ForeignKey(to='equity.Security')),
            ],
        ),
        migrations.AddField(
            model_name='security',
            name='secType',
            field=models.ForeignKey(to='equity.SecurityType'),
        ),
        migrations.AddField(
            model_name='position',
            name='secId',
            field=models.ForeignKey(to='equity.Security'),
        ),
        migrations.AddField(
            model_name='newrebalance',
            name='accounts',
            field=models.ForeignKey(default=b'ABC', to='equity.Account'),
        ),
    ]
