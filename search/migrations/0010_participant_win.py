# Generated by Django 3.1.7 on 2021-05-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20210512_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='win',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
