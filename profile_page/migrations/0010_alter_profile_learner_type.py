# Generated by Django 5.0.3 on 2024-03-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0009_profile_learner_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='learner_type',
            field=models.CharField(choices=[('Beginner', 'B'), ('Skilled', 'S'), ('Advanced', 'A')], default='An avid learner!', max_length=30),
        ),
    ]
