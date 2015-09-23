# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0002_investigation_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='person',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
