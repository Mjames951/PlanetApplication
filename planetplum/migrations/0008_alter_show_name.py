# Generated by Django 5.1.2 on 2025-01-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planetplum', '0007_alter_band_approved_alter_label_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='name',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Title'),
        ),
    ]