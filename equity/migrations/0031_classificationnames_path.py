# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0030_auto_20151129_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='path',
            field=models.CharField(default='stop', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
