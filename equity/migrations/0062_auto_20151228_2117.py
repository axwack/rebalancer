# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0061_usersecurityselectionmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersecurityselectionmodel',
            name='classificationNameNode',
            field=models.ForeignKey(to='equity.ClassificationNames', null=True),
        ),
    ]
