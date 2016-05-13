# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressUse',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPointSystem',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPointUse',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventTiming',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdentifierType',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdentifierUse',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NameUse',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuantityComparator',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SignatureType',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimingAbbreviation',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnitsOfTime',
            fields=[
                ('id', models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, serialize=False)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('display', models.CharField(max_length=255)),
                ('definition', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
