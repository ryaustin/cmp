# Generated by Django 4.2.5 on 2023-10-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cmp", "0003_remove_country_alpha2_remove_country_alpha3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="cioc",
            field=models.CharField(default="", max_length=3),
        ),
    ]
