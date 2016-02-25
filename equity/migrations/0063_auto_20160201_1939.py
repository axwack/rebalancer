# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0062_auto_20151228_2117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersecurityselectionmodel',
            old_name='hasChildnode',
            new_name='hasChildNode',
        ),
    ]
