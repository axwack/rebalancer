# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0002_auto_20151009_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationames',
            name='classificationLevel',
            field=models.IntegerField(),
        ),
    ]
