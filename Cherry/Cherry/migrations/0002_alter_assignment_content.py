# Generated by Django 4.2.5 on 2023-10-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='content',
            field=models.FileField(max_length=254, upload_to='students/'),
        ),
    ]
