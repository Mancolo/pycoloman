# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=25, blank=True)),
                ('phone_second', models.CharField(max_length=25, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('access_phone', models.BooleanField(default=False)),
                ('access_phys', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to='crm.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalContact',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=25, blank=True)),
                ('phone_second', models.CharField(max_length=25, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('access_phone', models.BooleanField(default=False)),
                ('access_phys', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('last_modified', models.DateTimeField(editable=False, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('company', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='crm.Customer', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contact',
            },
        ),
    ]
