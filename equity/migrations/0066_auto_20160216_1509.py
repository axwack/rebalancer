# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0065_auto_20160202_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersecurityselectionmodel',
            old_name='classificationNameNode',
            new_name='classificationName',
        ),
    ]
