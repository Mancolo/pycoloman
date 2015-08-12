# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20150812_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='role',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='kind',
            field=models.ForeignKey(blank=True, to='crm.CustomerKind', null=True),
        ),
        migrations.AlterField(
            model_name='historicalcontact',
            name='role',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
