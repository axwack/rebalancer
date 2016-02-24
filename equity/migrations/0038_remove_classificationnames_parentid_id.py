# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0037_auto_20151129_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='parentId_id',
        ),
    ]
