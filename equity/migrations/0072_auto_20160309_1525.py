# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('equity', '0071_auto_20160308_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 9, 15, 25, 35, 978031, tzinfo=utc),
                                       auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='lastModifyDate',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 9, 15, 25, 42, 649381, tzinfo=utc),
                                       auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='recordVersion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
