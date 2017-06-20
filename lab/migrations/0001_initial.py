# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_identifier', models.CharField(editable=False, max_length=25, unique=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('box_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('testing', 'Testing'), ('storage', 'Storage'), ('other', 'Other')], default='testing', max_length=25)),
                ('status', models.CharField(choices=[('open', 'Open'), ('verified', 'Verified'), ('packed', 'Packed'), ('shipped', 'Shipped')], default='open', max_length=15)),
                ('accept_primary', models.BooleanField(default=False, help_text="Tick to allow 'primary' specimens to be added to this box")),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoxItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('identifier', models.CharField(max_length=25)),
                ('comment', models.CharField(blank=True, max_length=25, null=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lab.Box')),
            ],
        ),
    ]
