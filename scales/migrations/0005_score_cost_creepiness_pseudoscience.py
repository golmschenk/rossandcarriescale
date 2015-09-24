# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0004_score_danger'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='cost',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='score',
            name='creepiness',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=6),
        ),
        migrations.AddField(
            model_name='score',
            name='pseudoscience',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=6),
        ),
    ]
