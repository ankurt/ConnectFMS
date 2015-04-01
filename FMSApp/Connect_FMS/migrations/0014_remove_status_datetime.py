# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0013_auto_20150331_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='datetime',
        ),
    ]
