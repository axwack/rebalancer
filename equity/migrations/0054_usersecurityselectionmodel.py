# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0053_taxlot_acctcd'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSecuritySelectionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tgtWeight', models.FloatField()),
                ('currWeight', models.FloatField()),
                ('hasChildnode', models.BooleanField()),
                ('ext_model_id', models.IntegerField()),
                ('securitySelectionModelName', models.ForeignKey(to='equity.SecuritySelectionModels')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
