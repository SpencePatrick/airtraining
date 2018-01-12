# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2018-01-05 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='question',
            name='figure1',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='question',
            name='figure2',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]