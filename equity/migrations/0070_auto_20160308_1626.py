# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0069_auto_20160307_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchanges',
            name='cntry_cd',
            field=models.ForeignKey(to='equity.Countries'),
        ),
    ]
