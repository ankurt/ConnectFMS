# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0006_auto_20150328_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='status_level',
            field=models.IntegerField(blank=True, choices=[(1, b'not resolved'), (2, b'in progress'), (3, b'resolved')], default=1),
        ),
    ]
