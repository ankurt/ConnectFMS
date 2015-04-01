# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0012_auto_20150330_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='zipcode',
            field=models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(b'^[0-9]{5}$', b'Only digits 0-9 are allowed.', b'Invalid zipcode')]),
        ),
    ]
