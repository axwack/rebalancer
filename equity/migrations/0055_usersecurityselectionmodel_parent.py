# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0054_usersecurityselectionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersecurityselectionmodel',
            name='parent',
            field=models.ForeignKey(related_name='children_set', to='equity.UserSecuritySelectionModel', null=True),
        ),
    ]
