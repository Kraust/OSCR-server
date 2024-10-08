# Generated by Django 4.2.9 on 2024-08-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combatlog', '0002_combatlog_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='damage_in',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='damage_out',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='heal_in',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='heal_out',
            field=models.JSONField(default=None, null=True),
        ),
    ]
