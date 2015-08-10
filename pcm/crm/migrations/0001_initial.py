# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zipcode', models.CharField(max_length=10, blank=True)),
                ('phone', models.CharField(max_length=25, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('locked', models.BooleanField(default=False)),
                ('number', models.CharField(max_length=20, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('closed_date', models.DateField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCustomer',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('state', models.CharField(max_length=2, blank=True)),
                ('zipcode', models.CharField(max_length=10, blank=True)),
                ('phone', models.CharField(max_length=25, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('locked', models.BooleanField(default=False)),
                ('number', models.CharField(max_length=20, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('closed_date', models.DateField(null=True, blank=True)),
                ('last_modified', models.DateTimeField(editable=False, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('kind', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='crm.CustomerKind', null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical customer',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCustomerKind',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('label', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical customer kind',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='kind',
            field=models.ForeignKey(to='crm.CustomerKind'),
        ),
    ]
