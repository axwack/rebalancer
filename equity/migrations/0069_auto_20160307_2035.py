# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0068_auto_20160307_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchanges',
            name='iso_exch_cd',
            field=models.CharField(default='NAS', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exchanges',
            name='mid_close_time',
            field=models.TimeField(null=True),
        ),
    ]
