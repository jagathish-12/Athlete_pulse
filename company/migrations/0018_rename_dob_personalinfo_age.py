# Generated by Django 4.2.15 on 2024-09-10 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0017_rename_blood_pressure_cardiodata_diastolic_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="personalinfo", old_name="DOB", new_name="age",
        ),
    ]
