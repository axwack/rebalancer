# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equity', '0006_auto_20151018_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocationmodels',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='allocationmodels',
            name='edited_by',
            field=models.ForeignKey(related_name='edited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
