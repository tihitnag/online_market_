# Generated by Django 4.2.6 on 2023-12-07 21:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0005_rename_catagory_item_catagory"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catagory",
            options={"ordering": ("name",), "verbose_name_plural": "Categories"},
        ),
        migrations.RenameField(
            model_name="item",
            old_name="catagory",
            new_name="category",
        ),
    ]
