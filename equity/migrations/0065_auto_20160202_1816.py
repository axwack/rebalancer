# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0064_securityselectionmodels_isparent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securityselectionmodels',
            name='isParent',
        ),
        migrations.AddField(
            model_name='usersecurityselectionmodel',
            name='isSSMNameNode',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
