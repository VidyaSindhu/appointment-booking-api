# Generated by Django 3.2.4 on 2021-10-16 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_staffschedule_specialist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffschedule',
            old_name='user',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='staffschedule',
            old_name='specialist',
            new_name='specialist_of',
        ),
    ]
