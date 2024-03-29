# Generated by Django 5.0.3 on 2024-03-18 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0009_alter_answer_is_correct'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.quiz')),
                ('selected_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
