# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0008_auto_20150328_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='utility',
            options={'ordering': ['name'], 'verbose_name_plural': 'utilities'},
        ),
    ]
