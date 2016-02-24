# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0032_auto_20151129_2103'),
    ]

    operations = [

        migrations.AddField(
            model_name='classificationnames',
            name='desc',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='sib_order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classificationnames',
            name='parent',
            field=models.ForeignKey(related_name='children_set', blank=True, to='equity.ClassificationNames',
                                    null=True),
        ),
    ]
