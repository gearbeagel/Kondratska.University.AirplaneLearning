# Generated by Django 5.0.3 on 2024-03-17 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_remove_lesson_lesson_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modules.quiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modules.lesson'),
            preserve_default=False,
        ),
    ]
