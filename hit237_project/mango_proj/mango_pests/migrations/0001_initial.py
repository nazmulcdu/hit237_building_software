# Generated by Django 5.2 on 2025-05-25 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('scientific_name', models.CharField(max_length=200)),
                ('short_desc', models.TextField()),
                ('full_desc', models.TextField()),
                ('image', models.ImageField(upload_to='pests/images/')),
            ],
        ),
        migrations.CreateModel(
            name='PestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=200)),
                ('pest_name', models.CharField(max_length=100)),
                ('observation', models.TextField()),
                ('image', models.ImageField(upload_to='pests/images/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('affected_part', models.CharField(max_length=100)),
                ('pest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='symptoms', to='mango_pests.pest')),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_organic', models.BooleanField(default=False)),
                ('pest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='mango_pests.pest')),
            ],
        ),
    ]
