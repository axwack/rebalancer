# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0019_remove_accountparameters_accountsincluded'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuritySelectionModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('securitySelectionModelName', models.CharField(max_length=100)),
                ('classificationNames', models.ManyToManyField(to='equity.ClassificationNames')),
            ],
        ),
    ]
