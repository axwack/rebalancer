# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0028_auto_20151127_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationnames',
            name='source',
            field=models.CharField(default=b'OWNER', max_length=100),
        ),
    ]
