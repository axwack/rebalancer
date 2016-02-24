# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0045_classificationnames_classificationname'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='classificationLevel',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
