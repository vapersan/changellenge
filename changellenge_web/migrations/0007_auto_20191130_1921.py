# Generated by Django 2.2.7 on 2019-11-30 19:21

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('changellenge_web', '0006_serviceaboutpreset_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceaboutpreset',
            name='preset',
            field=martor.models.MartorField(default='', max_length=50000, verbose_name='Preset'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serviceaboutpreset',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]
