# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scales', '0003_score_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='danger',
            field=models.DecimalField(decimal_places=4, max_digits=6, default=1),
        ),
    ]
