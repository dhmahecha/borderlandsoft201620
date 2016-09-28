# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val_imagen', models.CharField(help_text='URL de la imagen del album', max_length=1000, verbose_name='Imágen')),
                ('nom_album', models.CharField(help_text='Nombre del album', max_length=1000, verbose_name='Album')),
            ],
        ),
        migrations.CreateModel(
            name='Album_audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_artistico', models.CharField(max_length=200)),
                ('nom_pais', models.CharField(max_length=50)),
                ('nom_ciudad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Artista_album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Album')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_audio', models.CharField(help_text='Nombre del audio', max_length=1000, verbose_name='Audio')),
                ('val_imagen', models.CharField(help_text='URL de la imagen del audio', max_length=1000, verbose_name='Imágen')),
                ('val_recurso', models.CharField(help_text='URL del recurso del audio', max_length=1000, verbose_name='Recurso')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Artista')),
            ],
        ),
        migrations.AddField(
            model_name='album_audio',
            name='audio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Audio'),
        ),
    ]
