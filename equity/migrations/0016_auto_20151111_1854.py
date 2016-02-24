# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0015_auto_20151105_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountfilters',
            name='accountName',
        ),
        migrations.AddField(
            model_name='accountfilters',
            name='accountName',
            field=models.ManyToManyField(to='equity.Account'),
        ),
    ]
