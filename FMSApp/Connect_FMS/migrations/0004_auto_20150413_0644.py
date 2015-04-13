# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Connect_FMS', '0003_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.BooleanField(default=True)),
                ('status', models.ForeignKey(to='Connect_FMS.Status')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numvotes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(to='Connect_FMS.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={},
        ),
        migrations.RenameField(
            model_name='status',
            old_name='likes',
            new_name='numlikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='votes',
        ),
    ]
