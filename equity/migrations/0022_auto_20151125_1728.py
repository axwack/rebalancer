# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0021_auto_20151125_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityselectionmodels',
            name='securitySelectionModelName',
            field=models.CharField(max_length=100),
        ),
    ]
