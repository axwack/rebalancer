# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0046_classificationnames_classificationlevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='sib_order',
        ),
    ]
