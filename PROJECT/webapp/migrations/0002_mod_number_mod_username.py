# Generated by Django 4.0.4 on 2022-06-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mod',
            name='username',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]