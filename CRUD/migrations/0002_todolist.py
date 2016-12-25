# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask', models.CharField(max_length=200)),
                ('length', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.Todo')),
            ],
        ),
    ]
