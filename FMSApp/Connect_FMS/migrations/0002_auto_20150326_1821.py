# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Connect_FMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at', 'votes']},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-created_at', 'likes']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='utility',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='datetime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='datetime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='response',
            old_name='datetime',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='building',
            name='address',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='building',
            name='state',
            field=models.CharField(default=b'PA', max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connectict'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia '), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin '), (b'WY', b'Wyoming')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='street_1',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='zipcode',
            field=models.CharField(default=0, max_length=300, validators=[django.core.validators.RegexValidator(b'^[0-9]{5}$', b'Only digits 0-9 are allowed', b'Invalid zipcode')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 22, 21, 55, 653999, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(max_length=600, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/posts/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='status',
            name='image',
            field=models.ImageField(upload_to=b'images/statuses/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default=b'student', max_length=15, choices=[(b'admin', b'Administrator'), (b'student', b'Student'), (b'fms', b'FMS')]),
            preserve_default=True,
        ),
    ]