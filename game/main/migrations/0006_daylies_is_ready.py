# Generated by Django 4.2.1 on 2023-05-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_daylies_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='daylies',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
