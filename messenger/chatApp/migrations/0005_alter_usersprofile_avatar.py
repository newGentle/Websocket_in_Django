# Generated by Django 4.1.7 on 2023-03-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_alter_usersprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='avatar',
            field=models.ImageField(default='/media/default.jpg', upload_to='avatar_img'),
        ),
    ]
