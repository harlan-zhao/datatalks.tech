# Generated by Django 2.2 on 2019-07-14 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autochart', '0007_auto_20190714_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfile',
            old_name='session_time',
            new_name='time',
        ),
    ]
