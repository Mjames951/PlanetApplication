# Generated by Django 5.1.2 on 2025-01-09 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planetplum', '0005_rename_approved_show_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='valid',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='label',
            old_name='valid',
            new_name='approved',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='valid',
            new_name='approved',
        ),
    ]
