# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0024_classificationnames_parentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='parentId',
            field=models.ForeignKey(to='equity.ClassificationNames'),
        ),
    ]
