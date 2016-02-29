# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0055_usersecurityselectionmodel_parent'),
    ]

    operations = [

        migrations.RenameField(
            model_name='usersecurityselectionmodel',
            old_name='securitySelectionModelName',
            new_name='SSM',
        ),

        migrations.AddField(
            model_name='usersecurityselectionmodel',
            name='classificationNameNode',
            field=models.ForeignKey(default=1, to='equity.ClassificationNames'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='securityselectionmodels',
            name='securityselectionmodelname',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
