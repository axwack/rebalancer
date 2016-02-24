# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0043_remove_classificationnames_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='classificationName',
            field=models.CharField(max_length=100),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='classificationName',
        ),

    ]
