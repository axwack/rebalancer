# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0022_auto_20151125_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='parent',
            field=models.CharField(default='Temp', max_length=100),
            preserve_default=False,
        ),
    ]
