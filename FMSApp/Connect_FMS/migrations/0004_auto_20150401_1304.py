# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0003_auto_20150401_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images/statuses/'),
        ),
    ]
