# Generated by Django 4.2.5 on 2023-10-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cmp", "0004_alter_country_cioc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="tld",
            field=models.CharField(default="", max_length=10),
        ),
    ]
