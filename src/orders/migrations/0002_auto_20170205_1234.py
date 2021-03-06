# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0004_restaurant_is_ok'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_leader', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, default='')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.MenuItem')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='extendgroup',
            name='group',
        ),
        migrations.RemoveField(
            model_name='extendgroup',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.DeleteModel(
            name='ExtendGroup',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
