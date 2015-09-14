# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IP_Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(unique=True, max_length=120)),
                ('count', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'IP Addresses',
            },
        ),
        migrations.CreateModel(
            name='Referrer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referral_code', models.CharField(max_length=18, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('referral_code', models.CharField(unique=True, max_length=10, blank=True)),
                ('repeat_ip', models.BooleanField(default=False)),
                ('times_email_opened', models.IntegerField(default=0, null=True, blank=True)),
                ('ip_address', models.CharField(max_length=120, blank=True)),
                ('referrals', models.IntegerField(default=0)),
                ('referrer', models.ForeignKey(blank=True, to='users.Referrer', null=True)),
            ],
        ),
    ]
