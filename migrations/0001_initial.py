# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django_documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ODTTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=16, unique=True)),
                ('templateFile', models.FileField(help_text='Ac\xe1 va el archivo de formato ODT que ser\xe1 utilizado para generar el PDF. Si quieres saber m\xe1s revisa el booklet que se encuentra en esta direcci\xf3n: LINK', upload_to=django_documents.models.upload_prefix)),
            ],
        ),
    ]
