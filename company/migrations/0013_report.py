# Generated by Django 4.2.15 on 2024-09-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0012_register_status_alter_metric_endurance_results_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
