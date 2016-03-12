# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0067_auto_20160307_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='listExchCd',
            field=models.CharField(max_length=20),
        ),
    ]
