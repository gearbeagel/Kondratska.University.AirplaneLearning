# Generated by Django 5.0.3 on 2024-03-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0008_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='learner_type',
            field=models.CharField(choices=[('B', 'Beginner'), ('S', 'Skilled'), ('A', 'Advanced')], default='An avid learner!', max_length=30),
        ),
    ]
