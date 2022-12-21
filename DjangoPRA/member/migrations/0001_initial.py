# Generated by Django 4.1.4 on 2022-12-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("pass1", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20)),
                ("gender", models.IntegerField(default=0)),
                ("tel", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                ("picture", models.CharField(max_length=200)),
            ],
        ),
    ]
