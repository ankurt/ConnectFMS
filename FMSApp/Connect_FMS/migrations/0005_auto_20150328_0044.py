# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0004_auto_20150328_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='building',
            field=models.ForeignKey(blank=True, null=True, to='Connect_FMS.Building'),
        ),
    ]
