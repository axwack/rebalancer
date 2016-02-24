# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equity', '0011_allocationnodes_dependentnode'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountFilters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acctFilterName', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('accountName', models.ForeignKey(to='equity.Account')),
                ('created_by', models.ForeignKey(related_name='accountfilters_requests_created', default=b'1',
                                                 to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(related_name='accountfilters_requests_edited', default=b'1',
                                                to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='created_by',
            field=models.ForeignKey(related_name='allocationmodels_requests_created', default=b'1',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocationmodels',
            name='edited_by',
            field=models.ForeignKey(related_name='allocationmodels_requests_edited', default=b'1',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
