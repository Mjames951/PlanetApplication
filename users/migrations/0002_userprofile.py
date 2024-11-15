# Generated by Django 5.1.2 on 2024-10-29 22:19

import colorfield.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='userpfps/')),
                ('primary', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('secondary', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
