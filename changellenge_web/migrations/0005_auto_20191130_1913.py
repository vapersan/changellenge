# Generated by Django 2.2.7 on 2019-11-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changellenge_web', '0004_auto_20191130_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAboutPreset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Preset',
                'verbose_name_plural': "Preset's",
            },
        ),
        migrations.AlterField(
            model_name='services',
            name='date_release',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date released'),
        ),
    ]
