# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0002_auto_20150412_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=b'profilepic', blank=True),
            preserve_default=True,
        ),
    ]
