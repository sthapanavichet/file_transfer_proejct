# Generated by Django 5.0.7 on 2024-08-01 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_transfer_app', '0005_filetransfer_file_hash'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filetransfer',
            name='file_hash',
        ),
    ]
