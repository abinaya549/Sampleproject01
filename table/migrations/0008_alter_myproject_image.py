# Generated by Django 4.0.5 on 2022-06-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_myproject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
