# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0007_auto_20151018_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocationmodels',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='edited_by',
            field=models.ForeignKey(related_name='edited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
