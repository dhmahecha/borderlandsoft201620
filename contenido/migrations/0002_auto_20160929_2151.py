# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='fec_creacion_album',
            field=models.DateField(auto_now=True, help_text='Fecha de creación del album'),
        ),
        migrations.AddField(
            model_name='album_audio',
            name='fec_asociacion_audio',
            field=models.DateField(auto_now=True, help_text='Fecha de asociación de audio a album'),
        ),
        migrations.AddField(
            model_name='audio',
            name='fec_entrada_audio',
            field=models.DateField(auto_now=True, help_text='Fecha de subida del audio'),
        ),
        migrations.AlterField(
            model_name='album',
            name='val_imagen',
            field=models.CharField(blank=True, help_text='URL de la imagen del album', max_length=1000, verbose_name='Imágen'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='val_imagen',
            field=models.CharField(blank=True, help_text='URL de la imagen del audio', max_length=1000, verbose_name='Imágen'),
        ),
    ]
