# Generated by Django 4.0 on 2023-07-10 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='object_id',
        ),
    ]