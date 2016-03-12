# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0070_auto_20160308_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencies',
            name='calc_precision',
            field=models.FloatField(null=True),
        ),
    ]
