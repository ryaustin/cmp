# Generated by Django 4.2.5 on 2023-10-23 20:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cmp", "0010_rank"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rank",
            old_name="Abbr",
            new_name="Abbreviation",
        ),
    ]
