# Generated by Django 2.1 on 2019-11-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='snapchat',
            field=models.TextField(blank=True, null=True, verbose_name='SnapChat'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='mediaKitLink',
            field=models.TextField(blank=True, null=True, verbose_name='Media Kit'),
        ),
    ]
