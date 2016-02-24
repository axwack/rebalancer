# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0010_auto_20151023_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocationnodes',
            name='dependentNode',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
