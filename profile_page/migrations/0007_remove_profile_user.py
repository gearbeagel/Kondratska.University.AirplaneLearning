# Generated by Django 5.0.3 on 2024-03-17 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0006_alter_profile_groups_alter_profile_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
