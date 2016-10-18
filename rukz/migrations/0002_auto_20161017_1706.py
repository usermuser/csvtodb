# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rukz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rukzak',
            options={'ordering': ('naim',)},
        ),
        migrations.RemoveField(
            model_name='rukzak',
            name='img_link',
        ),
        migrations.RemoveField(
            model_name='rukzak',
            name='other',
        ),
        migrations.RemoveField(
            model_name='rukzak',
            name='price',
        ),
    ]
