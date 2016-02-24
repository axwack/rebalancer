# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0040_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='parentId_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
