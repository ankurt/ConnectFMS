# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(blank=True, max_length=300)),
                ('zipcode', models.CharField(max_length=300, validators=[django.core.validators.RegexValidator(b'^[0-9]{5}$', b'Only digits 0-9 are allowed.', b'Invalid zipcode')])),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connectict'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia '), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin '), (b'WY', b'Wyoming')], default=b'PA', max_length=2)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=600)),
                ('building', models.ForeignKey(blank=True, null=True, to='Connect_FMS.Building')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('votes', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to=b'images/posts/')),
                ('location', models.ForeignKey(to='Connect_FMS.Location')),
            ],
            options={
                'ordering': ['-created_at', '-votes'],
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_level', models.IntegerField(blank=True, choices=[(1, b'not resolved'), (2, b'in progress'), (3, b'resolved')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(blank=True, null=True, to='Connect_FMS.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to=b'images/statuses/')),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_at', 'likes'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('andrewid', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(choices=[(b'admin', b'Administrator'), (b'student', b'Student'), (b'fms', b'FMS')], default=b'student', max_length=15)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'utilities',
            },
        ),
        migrations.AddField(
            model_name='status',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
        ),
        migrations.AddField(
            model_name='status',
            name='utility',
            field=models.ForeignKey(to='Connect_FMS.Utility'),
        ),
        migrations.AddField(
            model_name='response',
            name='status',
            field=models.ForeignKey(blank=True, null=True, to='Connect_FMS.Status'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='utility',
            field=models.ForeignKey(to='Connect_FMS.Utility'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='Connect_FMS.User'),
        ),
    ]
