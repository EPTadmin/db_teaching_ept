# Generated by Django 4.2.6 on 2023-11-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0015_delete_personposition_activity_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Position_Activity",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Instituttleder", "Instituttleder"),
                            ("Nestleder forskning", "Nestleder forskning"),
                            ("Nestleder utdanning", "Nestleder utdanning"),
                            ("Faggruppeleder", "Faggruppeleder"),
                            ("Studieprogramleder", "Studieprogramleder"),
                            (
                                "Leder - forskningsprosjekt",
                                "Leder - forskningsprosjekt",
                            ),
                            (
                                "WP leder - Forskningsprosjekt",
                                "WP leder - Forskningsprosjekt",
                            ),
                            ("Leder - EU prosjekt", "Leder - EU prosjekt"),
                            ("WP leder - EU prosjekt", "WP leder - EU prosjekt"),
                            ("Antall PhD studenter", "Antall PhD studenter"),
                        ],
                        default="-",
                        max_length=40,
                    ),
                ),
                (
                    "emne",
                    models.CharField(
                        choices=[("L", "L"), ("P", "P")], default="-", max_length=2
                    ),
                ),
                (
                    "antall_time",
                    models.CharField(
                        blank=True,
                        choices=[("50", "50"), ("70", "70"), ("100", "100")],
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "arsverk",
                    models.CharField(
                        blank=True,
                        choices=[("20", "20"), ("80", "80")],
                        max_length=3,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
