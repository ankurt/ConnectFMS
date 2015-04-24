# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0007_auto_20150424_0017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['building+__name']},
        ),
    ]
