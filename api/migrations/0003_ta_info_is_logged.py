# Generated by Django 4.2.2 on 2023-06-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_ta_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="ta_info",
            name="is_logged",
            field=models.BooleanField(default=False),
        ),
    ]
