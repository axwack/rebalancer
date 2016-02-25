# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0056_auto_20151228_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersecurityselectionmodel',
            name='SSM',
        ),
        migrations.RemoveField(
            model_name='usersecurityselectionmodel',
            name='classificationNameNode',
        ),
        migrations.RemoveField(
            model_name='usersecurityselectionmodel',
            name='parent',
        ),
        migrations.DeleteModel(
            name='UserSecuritySelectionModel',
        ),
    ]
