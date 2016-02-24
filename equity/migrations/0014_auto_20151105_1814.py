# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0013_accountparameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountparameters',
            name='rebalanceName',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
