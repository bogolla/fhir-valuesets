# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('valuesets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeUnits',
            fields=[
                ('id', models.UUIDField(editable=False, serialize=False, default=uuid.uuid4, primary_key=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
