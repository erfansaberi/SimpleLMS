# Generated by Django 4.1.5 on 2023-01-31 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simple_LMS', '0012_notification_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='number',
            field=models.IntegerField(),
        ),
    ]
