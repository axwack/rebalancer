# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0031_classificationnames_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='numchild',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='path',
        ),
    ]
