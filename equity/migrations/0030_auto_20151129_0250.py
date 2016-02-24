# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0029_auto_20151128_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificationnames',
            name='level',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='classificationnames',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='depth',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),

        # migrations.AddField(
        #    model_name='classificationnames',
        #    name='path',
        #    field=models.CharField(unique=True, max_length=255, default='NULL'),
        #    preserve_default=False,
        # ),

        migrations.AlterField(
            model_name='classificationnames',
            name='parentId',
            field=models.ForeignKey(related_name='children_set', blank=True, to='equity.ClassificationNames',
                                    null=True),
        ),
    ]
