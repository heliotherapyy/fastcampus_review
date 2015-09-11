# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0003_auto_20150911_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='miniblog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(null=True, blank=True, to='miniblog.Tag'),
        ),
    ]
