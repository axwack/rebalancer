# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0004_auto_20151018_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocationmodels',
            name='id',
            field=models.IntegerField(serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='allocationnodes',
            name='id',
            field=models.IntegerField(serialize=False, auto_created=True, primary_key=True),
        ),
    ]
