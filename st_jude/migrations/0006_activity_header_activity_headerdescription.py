# Generated by Django 5.0.5 on 2024-07-05 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_jude', '0005_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='header',
            field=models.CharField(default='Default header', max_length=255),
        ),
        migrations.AddField(
            model_name='activity',
            name='headerDescription',
            field=models.CharField(default='Default headerDescription', max_length=255),
            preserve_default=False,
        ),
    ]
