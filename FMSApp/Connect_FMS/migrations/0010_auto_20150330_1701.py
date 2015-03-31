# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0009_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at', '-votes']},
        ),
        migrations.AlterModelOptions(
            name='utility',
            options={'ordering': ['name'], 'verbose_name_plural': 'utilities'},
        ),
    ]
