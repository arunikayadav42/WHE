# Generated by Django 2.2.6 on 2019-11-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20191103_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='snapchat',
        ),
        migrations.AlterField(
            model_name='artist',
            name='youtube',
            field=models.TextField(blank=True, null=True, verbose_name='YouTube'),
        ),
    ]
