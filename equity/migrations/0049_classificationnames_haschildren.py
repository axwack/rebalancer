# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0048_auto_20151130_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='classificationnames',
            name='hasChildren',
            field=models.BooleanField(default=False),
        ),
    ]
