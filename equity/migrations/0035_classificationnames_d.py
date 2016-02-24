# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0034_auto_20151129_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='d',
            field=models.CharField(default='Hello', max_length=255),
            preserve_default=False,
        ),
    ]
