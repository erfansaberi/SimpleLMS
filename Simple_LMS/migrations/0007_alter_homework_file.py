# Generated by Django 4.1.5 on 2023-01-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simple_LMS', '0006_alter_homework_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(upload_to='uploads/homeworks'),
        ),
    ]
