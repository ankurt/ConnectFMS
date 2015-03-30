# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0005_auto_20150328_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='post',
            field=models.ForeignKey(blank=True, null=True, to='Connect_FMS.Post'),
        ),
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.ForeignKey(blank=True, null=True, to='Connect_FMS.Status'),
        ),
        migrations.AlterField(
            model_name='response',
            name='status_level',
            field=models.IntegerField(blank=True, choices=[(1, b'not resolved'), (2, b'in progress'), (3, b'resolved')], default=1, max_length=2),
        ),
    ]
