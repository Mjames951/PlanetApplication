# Generated by Django 5.1.2 on 2025-01-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetplum', '0006_rename_valid_band_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='label',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
