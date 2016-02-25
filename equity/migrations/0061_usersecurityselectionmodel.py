# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0060_auto_20151228_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSecuritySelectionModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tgtWeight', models.FloatField()),
                ('currWeight', models.FloatField()),
                ('hasChildnode', models.BooleanField()),
                ('ext_model_id', models.IntegerField()),
                ('SSM', models.ForeignKey(to='equity.SecuritySelectionModels')),
                ('classificationNameNode', models.ForeignKey(to='equity.ClassificationNames')),
                ('parent', models.ForeignKey(related_name='children_set', to='equity.UserSecuritySelectionModel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
