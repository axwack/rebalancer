# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0014_auto_20151105_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountparameters',
            name='adjustCashAfterRebal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='adjustWgtAfterRebal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='reviewCurrentSale',
            field=models.BooleanField(default=False),
        ),
    ]
