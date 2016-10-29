# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160520022824 on 2016-07-02 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'problems')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('details', models.TextField()),
                ('review', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'problem')),
                ('options', models.ManyToManyField(to='log.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_compulsory', models.BooleanField(default=False)),
                ('length', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'quizzes')),
                ('questions', models.ManyToManyField(to='log.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='topics',
            field=models.ManyToManyField(to='log.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Option'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Quiz'),
        ),
    ]
