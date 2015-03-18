# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=600)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=600)),
                ('building', models.ForeignKey(to='Connect_FMS.Building')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('location', models.ForeignKey(to='Connect_FMS.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_level', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='Connect_FMS.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=600)),
                ('image', models.CharField(max_length=900)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('andrewid', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='status',
            name='utility',
            field=models.ForeignKey(to='Connect_FMS.Utility'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='response',
            name='status',
            field=models.ForeignKey(to='Connect_FMS.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='utility',
            field=models.ForeignKey(to='Connect_FMS.Utility'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
            preserve_default=True,
        ),
    ]
