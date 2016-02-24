# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0008_auto_20151018_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allocationmodels',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', default=b'1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='edited_by',
            field=models.ForeignKey(related_name='edited_by', default=b'1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='modelName',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='allocationnodes',
            name='allocationModel',
            field=models.ForeignKey(related_name='allocationNodes', to='equity.AllocationModels'),
        ),
        migrations.AlterField(
            model_name='allocationnodes',
            name='classificationName',
            field=models.ForeignKey(related_name='classificationNames', to='equity.ClassificationNames'),
        ),
    ]
