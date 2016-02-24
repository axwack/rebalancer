# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0026_auto_20151127_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='tree_id',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classificationnames',
            name='parentId',
            field=mptt.fields.TreeForeignKey(blank=True, to='equity.ClassificationNames', null=True),
        ),
    ]
