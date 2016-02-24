# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0049_classificationnames_haschildren'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classificationnames',
            old_name='hasChildren',
            new_name='hasChildNode',
        ),
    ]
