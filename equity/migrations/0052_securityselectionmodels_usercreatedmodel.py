# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0051_auto_20151204_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='securityselectionmodels',
            name='userCreatedModel',
            field=models.TextField(default='Hello'),
            preserve_default=False,
        ),
    ]
