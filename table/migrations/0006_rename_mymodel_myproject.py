# Generated by Django 4.0.5 on 2022-06-21 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_rename_student_mymodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyModel',
            new_name='MyProject',
        ),
    ]
