# Generated by Django 5.1.4 on 2024-12-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_orders"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="phone",
            field=models.CharField(default="", max_length=50),
        ),
    ]
