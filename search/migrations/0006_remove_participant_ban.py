# Generated by Django 3.1.7 on 2021-05-12 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20210511_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='ban',
        ),
    ]
