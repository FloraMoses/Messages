# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='msg_id',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='user_id',
            new_name='user',
        ),
    ]
