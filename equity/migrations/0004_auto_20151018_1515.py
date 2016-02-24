# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0003_auto_20151014_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocationModels',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('modelName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AllocationNodes',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('level', models.IntegerField()),
                ('allocationModel', models.ForeignKey(to='equity.AllocationModels')),
            ],
        ),
        migrations.AlterField(
            model_name='classificationnames',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='allocationnodes',
            name='classificationName',
            field=models.ForeignKey(to='equity.ClassificationNames'),
        ),
    ]
