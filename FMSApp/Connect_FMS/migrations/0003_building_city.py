# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0002_auto_20150327_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
