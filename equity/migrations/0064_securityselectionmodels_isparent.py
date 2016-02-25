# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0063_auto_20160201_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='securityselectionmodels',
            name='isParent',
            field=models.BooleanField(default=True),
        ),
    ]
