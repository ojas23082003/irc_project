# Generated by Django 2.2 on 2022-10-30 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_customer_owner_rest_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rest_info',
            new_name='Resto',
        ),
    ]
