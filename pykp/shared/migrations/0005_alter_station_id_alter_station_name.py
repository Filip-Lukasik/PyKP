# Generated by Django 5.0 on 2023-12-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shared", "0004_alter_location_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="station",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="station",
            name="name",
            field=models.TextField(),
        ),
    ]
