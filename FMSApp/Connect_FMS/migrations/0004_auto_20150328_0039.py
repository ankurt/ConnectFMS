# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0003_building_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='building',
            field=models.ForeignKey(blank=True, to='Connect_FMS.Building'),
        ),
    ]
