# Generated by Django 4.1.3 on 2022-11-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_alter_event_precursor_alter_organizer_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="competitors",
            field=models.ManyToManyField(related_name="event", to="events.competitor"),
        ),
        migrations.AlterField(
            model_name="event",
            name="subjects",
            field=models.ManyToManyField(related_name="event", to="events.subject"),
        ),
    ]
