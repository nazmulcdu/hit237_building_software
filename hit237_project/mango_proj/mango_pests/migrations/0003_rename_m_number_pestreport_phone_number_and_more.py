# Generated by Django 5.2.1 on 2025-05-27 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mango_pests", "0002_pestreport_affected_farm_area_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pestreport",
            old_name="m_number",
            new_name="phone_number",
        ),
        migrations.RenameField(
            model_name="pestreport",
            old_name="severe_lvl",
            new_name="severity_level",
        ),
    ]
