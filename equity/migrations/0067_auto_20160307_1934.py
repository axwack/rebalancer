# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equity', '0066_auto_20160216_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cntry_cd', models.CharField(max_length=100, null=True)),
                ('cntry_name', models.CharField(max_length=1000)),
                ('iso_cntry_cd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('currencyCd', models.CharField(max_length=100, null=True)),
                ('currencyName', models.CharField(max_length=100, null=True)),
                ('calc_precision', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Exchanges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exch_cd', models.CharField(unique=True, max_length=200)),
                ('exchange', models.CharField(max_length=1000)),
                ('exch_or_otc', models.CharField(max_length=5)),
                ('tz_region', models.CharField(max_length=10)),
                ('open_time', models.TimeField(null=True)),
                ('mid_open_time', models.TimeField(null=True)),
                ('cutoff_time', models.TimeField(null=True)),
                ('close_time', models.TimeField(null=True)),
                ('cntry_cd', models.OneToOneField(to='equity.Countries')),
            ],
        ),
        migrations.RemoveField(
            model_name='security',
            name='identity',
        ),
        migrations.AddField(
            model_name='security',
            name='benchmarkSecurity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='comments',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='countryOfRisk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='crossCurrencyCd',
            field=models.CharField(default='USD', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='cusip',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='divCurrency',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='extSecId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='isin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='issueState',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='lastModifyBy',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='locCurrencyCd',
            field=models.CharField(default='USD', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='sedol',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='shortName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='strikePrice',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='ticker',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='valoran',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificationnames',
            name='classificationName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rebalanceparameters',
            name='taxLots',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='listExchCd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taxlot',
            name='extTaxLotId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='security',
            name='issueCountry',
            field=models.ForeignKey(default='1', to='equity.Countries'),
            preserve_default=False,
        ),
    ]
