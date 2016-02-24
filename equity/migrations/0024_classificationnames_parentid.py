# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0023_classificationnames_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='parentId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
