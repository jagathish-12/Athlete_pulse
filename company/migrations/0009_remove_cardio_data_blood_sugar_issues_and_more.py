# Generated by Django 4.2.15 on 2024-09-03 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0008_cardio_data"),
    ]

    operations = [
        migrations.RemoveField(model_name="cardio_data", name="blood_sugar_issues",),
        migrations.AddField(
            model_name="cardio_data",
            name="bloodSugarIssues",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
