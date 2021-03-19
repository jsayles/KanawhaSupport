# Generated by Django 3.0.4 on 2020-03-15 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import support.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=32, unique=True)),
                ('address1', models.CharField(blank=True, max_length=128)),
                ('address2', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(blank=True, max_length=128)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('admin_email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(blank=True, max_length=16)),
                ('website', models.URLField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to=support.models.space_logo_path)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=16)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=support.models.user_photo_path)),
                ('valid_billing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
                'get_latest_by': 'last_modified',
            },
        ),
    ]