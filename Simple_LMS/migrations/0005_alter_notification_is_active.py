# Generated by Django 4.1.5 on 2023-01-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simple_LMS', '0004_remove_notification_image_notification_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='is_active',
            field=models.BooleanField(),
        ),
    ]
