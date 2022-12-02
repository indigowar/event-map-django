# Generated by Django 4.1.3 on 2022-12-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FoundingType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="event",
            name="founding_type",
        ),
        migrations.AddField(
            model_name="event",
            name="founding_type",
            field=models.ManyToManyField(
                related_name="event", to="events.foundingtype"
            ),
        ),
    ]
