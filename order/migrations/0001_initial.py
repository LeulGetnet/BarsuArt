# Generated by Django 4.2 on 2025-02-08 18:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('sample_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('wanted_size', models.CharField(max_length=20)),
                ('style', models.CharField(choices=[('detailed', 'Detailed'), ('abstract', 'Abstract')], max_length=50)),
                ('email_or_phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderFormDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=False, max_length=30, null=False)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
