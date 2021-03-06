# Generated by Django 3.1.7 on 2021-03-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20210313_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='summoner',
            name='account_id',
            field=models.CharField(default=0, max_length=56),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summoner',
            name='puuid',
            field=models.CharField(default=1, max_length=78),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='summoner',
            name='summoner_id',
            field=models.CharField(default=1, max_length=63),
            preserve_default=False,
        ),
    ]
