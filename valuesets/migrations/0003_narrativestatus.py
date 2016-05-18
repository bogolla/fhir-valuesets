# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('valuesets', '0002_ageunits'),
    ]

    operations = [
        migrations.CreateModel(
            name='NarrativeStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
