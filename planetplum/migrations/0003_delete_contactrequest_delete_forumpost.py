# Generated by Django 5.1.2 on 2024-11-21 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planetplum', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactrequest',
        ),
        migrations.DeleteModel(
            name='forumpost',
        ),
    ]