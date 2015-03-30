# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0009_auto_20150330_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='street_1',
            new_name='street',
        ),
    ]
