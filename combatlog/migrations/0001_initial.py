# Generated by Django 4.2.9 on 2024-04-13 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Metadata",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("map", models.TextField()),
                ("difficulty", models.TextField(default=None, null=True)),
                ("summary", models.JSONField()),
                ("date_time", models.DateTimeField(default=None, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CombatLog",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.TextField(default=None, null=True)),
                (
                    "metadata",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="combatlog.metadata",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
