# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0020_securityselectionmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityselectionmodels',
            name='securitySelectionModelName',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
