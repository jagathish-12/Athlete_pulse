# Generated by Django 4.2.15 on 2024-09-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0010_alter_cardio_data_bloodsugarissues_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="metric",
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
                (
                    "existing_medical_conditions",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        help_text="Do you have any existing medical conditions?",
                        max_length=30,
                    ),
                ),
                ("medical_conditions", models.CharField(max_length=200)),
                (
                    "training_intensity",
                    models.CharField(
                        choices=[
                            ("High", "High"),
                            ("Moderate", "Moderate"),
                            ("Low", "Low"),
                        ],
                        default="Moderate",
                        help_text="How would you describe your training intensity levels?",
                        max_length=20,
                    ),
                ),
                ("endurance_results", models.CharField(max_length=200)),
                (
                    "sleep_patterns",
                    models.CharField(
                        choices=[
                            ("Less than 4 hours", "Less than 4 hours"),
                            ("4-6 hours", "4-6 hours"),
                            ("6-8 hours", "6-8 hours"),
                            ("More than 8 hours", "More than 8 hours"),
                        ],
                        default="6-8 hours",
                        help_text="How many hours do you sleep on average per night?",
                        max_length=20,
                    ),
                ),
                ("training_regimen", models.CharField(max_length=400)),
                (
                    "injury_during_training",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")],
                        default="No",
                        help_text="Have you experienced any injuries during competition or training?",
                        max_length=30,
                    ),
                ),
                (
                    "injury_description",
                    models.TextField(
                        blank=True,
                        help_text="Please describe the type, severity, and treatment of your injury.",
                        max_length=200,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="cardio_data",
            name="cardiac_events",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Arrhythmias", "Arrhythmias"),
                    (
                        "Myocardial Infarction (Heart Attack)",
                        "Myocardial Infarction (Heart Attack)",
                    ),
                    ("Angina Pectoris", "Angina Pectoris"),
                    ("No Events", "No Events"),
                    (
                        "Congestive Heart Failure (CHF)",
                        "Congestive Heart Failure (CHF)",
                    ),
                    ("Stroke", "Stroke"),
                    ("Coronary Artery Disease (CAD)", "Coronary Artery Disease (CAD)"),
                    ("Cardiomyopathy", "Cardiomyopathy"),
                ],
                default="No Events",
                help_text="Select any previous cardiac events you have experienced.",
                max_length=255,
                null=True,
            ),
        ),
    ]