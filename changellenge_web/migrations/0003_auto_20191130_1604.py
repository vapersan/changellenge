# Generated by Django 2.2.7 on 2019-11-30 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('changellenge_web', '0002_auto_20191130_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesrelation',
            name='children',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Children', to='changellenge_web.Services', verbose_name='Children'),
        ),
    ]
