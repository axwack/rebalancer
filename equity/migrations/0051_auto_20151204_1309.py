# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0050_auto_20151204_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='hasChildNode',
            field=models.NullBooleanField(default=False),
        ),
    ]
