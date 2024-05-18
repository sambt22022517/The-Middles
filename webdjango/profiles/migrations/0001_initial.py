# Generated by Django 5.0.3 on 2024-04-19 17:19

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('email_verify', models.EmailField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, max_length=12, null=True)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(blank=True, upload_to='avatar')),
                ('city', models.CharField(blank=True, max_length=255)),
                ('district', models.CharField(blank=True, max_length=255)),
                ('country_of_residence', models.CharField(blank=True, max_length=255)),
                ('hobby', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
