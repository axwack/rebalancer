# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0033_auto_20151129_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='parent',
            field=models.ForeignKey(related_name='children_set', to='equity.ClassificationNames', null=True),
        ),
    ]
