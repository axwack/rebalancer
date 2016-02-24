# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0035_classificationnames_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='d',
        ),
    ]
