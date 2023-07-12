# Generated by Django 4.2.2 on 2023-07-03 03:46

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]
