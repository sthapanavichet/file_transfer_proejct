# Generated by Django 4.2.6 on 2023-11-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_transfer_app', '0004_remove_filetransfer_encrypted_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='filetransfer',
            name='file_hash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
