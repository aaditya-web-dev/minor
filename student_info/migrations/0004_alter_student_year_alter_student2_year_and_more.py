# Generated by Django 5.0.3 on 2024-11-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0003_student2_student3_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(default='1st year', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student2',
            name='year',
            field=models.CharField(default='2nd year', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student3',
            name='year',
            field=models.CharField(default='3rd year', max_length=255, null=True),
        ),
    ]