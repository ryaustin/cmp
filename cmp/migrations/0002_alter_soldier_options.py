# Generated by Django 4.2.7 on 2023-11-17 15:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cmp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="soldier",
            options={"ordering": ["surname"]},
        ),
    ]
