# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equity', '0052_securityselectionmodels_usercreatedmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxlot',
            name='acctCd',
            field=models.ForeignKey(default='Acct1', to='equity.Account'),
            preserve_default=False,
        ),
    ]
