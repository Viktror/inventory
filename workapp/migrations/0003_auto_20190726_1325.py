# Generated by Django 2.2.3 on 2019-07-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0002_tools_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tools',
            new_name='Tool',
        ),
    ]
