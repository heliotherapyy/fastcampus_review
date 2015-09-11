# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0002_auto_20150910_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='miniblog.Post', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='miniblog.Category', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ForeignKey(to='miniblog.Tag', default=''),
            preserve_default=False,
        ),
    ]
