# Generated by Django 2.2 on 2022-10-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_mod_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mod',
        ),
    ]