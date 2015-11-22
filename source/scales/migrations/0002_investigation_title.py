# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
