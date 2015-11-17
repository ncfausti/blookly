# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20151025_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
        ),
    ]
