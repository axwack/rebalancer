# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0042_remove_classificationnames_parentid_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='source',
        ),
    ]
