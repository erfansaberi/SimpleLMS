# Generated by Django 4.1.5 on 2023-01-30 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simple_LMS', '0003_rename_homeworks_homework_rename_notes_note_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='image',
        ),
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
    ]
