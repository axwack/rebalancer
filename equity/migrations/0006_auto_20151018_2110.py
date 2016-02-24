# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0005_auto_20151018_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocationmodels',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='allocationnodes',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
