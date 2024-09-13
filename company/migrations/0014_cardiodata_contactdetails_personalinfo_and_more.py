# Generated by Django 4.2.15 on 2024-09-08 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0013_report"),
    ]

    operations = [
        migrations.CreateModel(
            name="CardioData",
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
                ("resting_heart_rate", models.CharField(max_length=30)),
                ("max_heart_rate", models.CharField(max_length=30)),
                ("blood_pressure", models.CharField(max_length=30)),
                ("vo2_max", models.CharField(max_length=30)),
                ("hrv", models.CharField(max_length=30)),
                ("recovery_time", models.CharField(max_length=30)),
                ("cardiacOutput", models.CharField(max_length=30)),
                ("ldlCholesterol", models.CharField(max_length=30)),
                ("hdlCholesterol", models.CharField(max_length=30)),
                ("triglycerides", models.CharField(max_length=30)),
                ("fastingBloodSugar", models.CharField(max_length=30)),
                ("postprandialBloodSugar", models.CharField(max_length=30)),
                ("familyHistory", models.CharField(max_length=30)),
                ("cardiacEvents", models.CharField(max_length=30)),
                (
                    "bloodSugarIssues",
                    models.CharField(
                        blank=True,
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="no",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "blood_sugar_condition",
                    models.CharField(
                        blank=True,
                        help_text="Specify the condition if blood sugar issues are present.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "family_history",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("No Known Family History", "No Known Family History"),
                            ("Single Case in Family", "Single Case in Family"),
                            ("Multiple Cases in Family", "Multiple Cases in Family"),
                            (
                                "Early Onset Cardiovascular Disease",
                                "Early Onset Cardiovascular Disease",
                            ),
                            (
                                "Genetic Cardiovascular Disorders",
                                "Genetic Cardiovascular Disorders",
                            ),
                        ],
                        default="No Known Family History",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "cardiac_events",
                    models.CharField(
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
                            (
                                "Coronary Artery Disease (CAD)",
                                "Coronary Artery Disease (CAD)",
                            ),
                            ("Cardiomyopathy", "Cardiomyopathy"),
                        ],
                        default="No Events",
                        help_text="Select any previous cardiac events you have experienced.",
                        max_length=255,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContactDetails",
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
                ("email", models.EmailField(max_length=30)),
                ("message", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="PersonalInfo",
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
                ("height", models.CharField(max_length=30)),
                ("weight", models.CharField(max_length=30)),
                ("age", models.CharField(max_length=30)),
                ("nationality", models.CharField(max_length=30)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=10,
                    ),
                ),
                (
                    "competition_level",
                    models.CharField(
                        choices=[
                            ("recreational", "Recreational"),
                            ("amateur", "Amateur"),
                            ("semi-professional", "Semi-Professional"),
                            ("professional", "Professional"),
                            ("elite-international", "Elite/International"),
                        ],
                        default="amateur",
                        max_length=50,
                    ),
                ),
                (
                    "training_frequency",
                    models.CharField(
                        choices=[
                            ("low", "Low: 1-3 hours per week"),
                            ("moderate", "Moderate: 4-7 hours per week"),
                            ("high", "High: 8-12 hours per week"),
                            ("very-high", "Very High: 13-20 hours per week"),
                            ("elite", "Elite: 21+ hours per week"),
                        ],
                        default="moderate",
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="cardio_data",),
        migrations.DeleteModel(name="contact_details",),
        migrations.DeleteModel(name="personal_info",),
        migrations.AddField(
            model_name="metric",
            name="report",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="company.report",
            ),
        ),
        migrations.AlterField(
            model_name="report", name="email", field=models.EmailField(max_length=30),
        ),
        migrations.AddField(
            model_name="personalinfo",
            name="report",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="personal_info",
                to="company.report",
            ),
        ),
        migrations.AddField(
            model_name="cardiodata",
            name="report",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cardio_data",
                to="company.report",
            ),
        ),
    ]