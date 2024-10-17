# Generated by Django 5.1.2 on 2024-10-17 19:55

import colorfield.fields
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contactrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='devlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='labelimages/')),
                ('description', models.TextField(blank=True, help_text='A description about the label', null=True)),
                ('link', models.URLField(blank=True, help_text='Does the label have a website or main social media?', null=True)),
                ('email', models.EmailField(blank=True, help_text='email for contacting the label', max_length=254, null=True)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='showVibe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('ageRange', models.CharField(choices=[('A', 'All Ages'), ('8', '18+'), ('9', '19+'), ('2', '21+')], default='A', max_length=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='venueimages/')),
                ('description', models.TextField(blank=True, help_text='Information on the venue or things people should know.', null=True, verbose_name='Information')),
                ('dm', models.BooleanField(default=False, help_text="Check the box if the address isn't public knowledge.", verbose_name='Ask a punk for the address')),
            ],
        ),
        migrations.CreateModel(
            name='forumpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('image', models.ImageField(blank=True, null=True, upload_to='forumimages/')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='planetplum.forumpost')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('picture', models.ImageField(upload_to='bandpfps/')),
                ('description', models.TextField(blank=True, null=True)),
                ('valid', models.BooleanField(default=True)),
                ('associates', models.ManyToManyField(related_name='associated', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='bands', to=settings.AUTH_USER_MODEL)),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planetplum.label')),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='userpfps/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='showposters/', verbose_name='Poster')),
                ('name', models.CharField(max_length=45, verbose_name='Title')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('valid', models.BooleanField(default=True)),
                ('bands', models.ManyToManyField(blank=True, help_text='(Not Required) choose which local bands are playing this show', to='planetplum.band', verbose_name='Local Bands Playing:')),
                ('venue', models.ForeignKey(help_text="what's the name of the show location? **DON'T PUT AN ADDRESS HERE**", on_delete=django.db.models.deletion.RESTRICT, to='planetplum.venue')),
            ],
            options={
                'ordering': ['-date', 'name'],
            },
        ),
    ]
