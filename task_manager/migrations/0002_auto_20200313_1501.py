# Generated by Django 3.0.2 on 2020-03-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='task',
            field=models.ManyToManyField(related_name='tags', to='task_manager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(related_name='tasks', to='task_manager.Tag'),
        ),
    ]
