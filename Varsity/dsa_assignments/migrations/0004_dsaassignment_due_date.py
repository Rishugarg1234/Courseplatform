# Generated by Django 5.2 on 2025-04-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsa_assignments', '0003_dsastudentsubmission_delete_dsasubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='dsaassignment',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
