# Generated by Django 4.1.5 on 2023-01-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simple_LMS', '0009_alter_homework_solution_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(upload_to='homeworks'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='solution_file',
            field=models.FileField(blank=True, null=True, upload_to='solutions'),
        ),
        migrations.AlterField(
            model_name='note',
            name='file',
            field=models.FileField(upload_to='notes'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='file',
            field=models.FileField(upload_to='', verbose_name='studentsolutions'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos'),
        ),
    ]
