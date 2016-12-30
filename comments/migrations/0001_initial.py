# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import django.utils.timezone
from django.conf import settings
import comments.utils


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('data', comments.utils.JSONField(null=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(related_name='comments', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, to='comments.Comment', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('comment', models.ForeignKey(related_name='versions', to='comments.Comment')),
                ('posting_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'get_latest_by': 'date_posted',
            },
        ),
    ]