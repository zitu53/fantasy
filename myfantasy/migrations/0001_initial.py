# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=10)),
                ('goals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('played', models.IntegerField(default=0)),
                ('won', models.IntegerField(default=0)),
                ('drawn', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('gd', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='myfantasy.Team'),
            preserve_default=True,
        ),
    ]
