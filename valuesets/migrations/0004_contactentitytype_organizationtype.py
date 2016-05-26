# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('valuesets', '0003_narrativestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactentityType',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, serialize=False, default=uuid.uuid4)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
