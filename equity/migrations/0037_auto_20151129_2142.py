# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0036_auto_20151129_2141'),
    ]

    operations = [

        # migrations.AddField(
        #     model_name='classificationNames',
        #     name='classificationLevel',
        #     field=models.IntegerField(default='1'),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #    model_name='classificationNames',
        #    name='parentId_id',
        #    field=models.IntegerField(default='1'),
        #    preserve_default=False,
        # ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='classificationLevel',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='parentId',
        ),
    ]
