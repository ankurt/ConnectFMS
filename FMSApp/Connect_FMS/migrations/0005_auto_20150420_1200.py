# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0004_auto_20150414_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='numvotes',
        ),
        migrations.AddField(
            model_name='votes',
            name='vote',
            field=models.IntegerField(default=0, choices=[(1, b'upvote'), (0, b'novote'), (-1, b'downvote')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/posts/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/statuspics/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=b'images/profilepics/%Y/%m/%d', blank=True),
            preserve_default=True,
        ),
    ]
