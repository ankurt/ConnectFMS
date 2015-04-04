# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=300, blank=True)),
                ('zipcode', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(b'^[0-9]{5}$', b'Only digits 0-9 are allowed.', b'Invalid zipcode')])),
                ('city', models.CharField(max_length=100, blank=True)),
                ('state', models.CharField(default=b'PA', max_length=2, blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connectict'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia '), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin '), (b'WY', b'Wyoming')])),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=600, blank=True)),
                ('building', models.ForeignKey(blank=True, to='Connect_FMS.Building', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to=b'images/posts/', blank=True)),
                ('location', models.ForeignKey(to='Connect_FMS.Location')),
            ],
            options={
                'ordering': ['-created_at', '-votes'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Connect_FMS.Comment')),
                ('post', models.ForeignKey(to='Connect_FMS.Post')),
            ],
            options={
                'abstract': False,
            },
            bases=('Connect_FMS.comment',),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_level', models.IntegerField(default=1, blank=True, choices=[(1, b'not resolved'), (2, b'in progress'), (3, b'resolved')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, to='Connect_FMS.Post', null=True)),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/statuses/', blank=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at', 'likes'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StatusComment',
            fields=[
                ('comment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Connect_FMS.Comment')),
                ('status', models.ForeignKey(to='Connect_FMS.Status')),
            ],
            options={
                'abstract': False,
            },
            bases=('Connect_FMS.comment',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('andrewid', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(default=b'student', max_length=15, choices=[(b'admin', b'Administrator'), (b'student', b'Student'), (b'fms', b'FMS')])),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
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
                'ordering': ['name'],
                'verbose_name_plural': 'utilities',
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
            field=models.ForeignKey(blank=True, to='Connect_FMS.Status', null=True),
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
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_connect_fms.comment_set', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
            preserve_default=True,
        ),
    ]
