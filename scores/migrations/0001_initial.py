# Generated by Django 2.2.9 on 2020-02-17 10:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("candidate", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Scores",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(0.0),
                            django.core.validators.MaxValueValidator(100.0),
                        ]
                    ),
                ),
                (
                    "candidate_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="candidate.Candidate",
                    ),
                ),
            ],
        ),
    ]
