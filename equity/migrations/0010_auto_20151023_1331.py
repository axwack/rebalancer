# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0009_auto_20151023_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allocationmodels',
            options={'ordering': ['modelName']},
        ),
        migrations.AlterField(
            model_name='allocationnodes',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='classificationnames',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
