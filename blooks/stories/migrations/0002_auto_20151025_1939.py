# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.ForeignKey(related_name='stories', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
