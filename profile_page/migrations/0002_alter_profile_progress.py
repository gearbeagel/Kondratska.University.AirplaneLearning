# Generated by Django 5.0.3 on 2024-03-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]