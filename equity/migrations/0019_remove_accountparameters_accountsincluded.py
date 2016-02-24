# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0018_auto_20151119_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountparameters',
            name='accountsIncluded',
        ),
    ]
