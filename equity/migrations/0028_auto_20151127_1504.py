# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0027_auto_20151127_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='parentId',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='equity.ClassificationNames',
                                             null=True),
        ),
    ]
