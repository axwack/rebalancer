# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0047_auto_20151130_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='classificationLevel',
            field=models.IntegerField(null=True),
        ),
    ]
