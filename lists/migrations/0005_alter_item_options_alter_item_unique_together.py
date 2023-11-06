# Generated by Django 4.2.1 on 2023-11-06 05:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0004_item_list"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ("id",)},
        ),
        migrations.AlterUniqueTogether(
            name="item",
            unique_together={("list", "text")},
        ),
    ]