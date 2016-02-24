# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0025_auto_20151127_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='parentId',
            field=models.ForeignKey(to='equity.ClassificationNames', null=True),
        ),
    ]
