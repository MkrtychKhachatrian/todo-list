# Generated by Django 4.2.1 on 2023-05-25 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0004_rename_status_task_done"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="done",
            new_name="is_done",
        ),
    ]
