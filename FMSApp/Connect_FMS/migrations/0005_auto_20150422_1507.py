# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0004_auto_20150414_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to=b'images/posts/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.FileField(null=True, upload_to=b'images/statuspics/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to=b'images/profilepics/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
