# Generated by Django 5.0.3 on 2024-03-21 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0012_remove_quiz_status_lessonstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='status',
        ),
    ]
