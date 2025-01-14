# Generated by Django 5.0.3 on 2024-11-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0002_remove_student_id_alter_student_rollno'),
    ]

    operations = [
        migrations.CreateModel(
            name='student2',
            fields=[
                ('photo', models.FileField(max_length=255, upload_to='student/')),
                ('name', models.CharField(max_length=255)),
                ('rollno', models.IntegerField(primary_key='true', serialize=False)),
                ('dob', models.DateField(null=True)),
                ('year', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='student3',
            fields=[
                ('photo', models.FileField(max_length=255, upload_to='student/')),
                ('name', models.CharField(max_length=255)),
                ('rollno', models.IntegerField(primary_key='true', serialize=False)),
                ('dob', models.DateField(null=True)),
                ('year', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.CharField(max_length=255, null=True),
        ),
    ]