# Generated by Django 5.0.3 on 2024-03-13 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_language_joke'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_type',
        ),
    ]
