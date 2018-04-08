# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-20 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('birth_time', models.DateTimeField()),
                ('work', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('bedroom', models.CharField(max_length=50)),
                ('domicile', models.CharField(max_length=400)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourclass.Beclass')),
                ('hobbys', models.ManyToManyField(blank=True, to='ourclass.Hobby')),
            ],
        ),
    ]