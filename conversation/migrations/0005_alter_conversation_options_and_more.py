# Generated by Django 4.2.6 on 2023-12-09 13:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("conversation", "0004_rename_convesation_convesationmessage_conversation"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="conversation",
            options={"ordering": ("-modified_at",)},
        ),
        migrations.RenameField(
            model_name="conversation",
            old_name="modifed_at",
            new_name="modified_at",
        ),
    ]
