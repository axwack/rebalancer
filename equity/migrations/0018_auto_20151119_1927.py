# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0017_auto_20151116_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountparameters',
            name='tradingCash',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='accountparameters',
            name='excludeClassification',
        ),
        migrations.AddField(
            model_name='accountparameters',
            name='excludeClassification',
            field=models.ManyToManyField(to='equity.ClassificationNames'),
        ),
    ]
