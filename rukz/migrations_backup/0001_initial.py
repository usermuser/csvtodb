# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rukzak',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=200)),
                ('naim', models.CharField(max_length=200, db_index=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('img_link', models.CharField(max_length=200)),
                ('other', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'ordering': ('price',),
            },
        ),
    ]
