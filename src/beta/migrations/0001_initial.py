# Generated by Django 3.0.8 on 2020-09-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ThreeFourFactor",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("period", models.CharField(max_length=10)),
                ("interval", models.CharField(max_length=8)),
                ("currency", models.CharField(max_length=3)),
                ("region", models.CharField(max_length=21)),
                (
                    "mktrf",
                    models.DecimalField(decimal_places=8, max_digits=10, null=True),
                ),
                ("smb", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("hml", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("mom", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                "ordering": ("-period",),
                "unique_together": {("period", "interval", "currency", "region")},
            },
        ),
        migrations.CreateModel(
            name="RiskFreeRate",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("period", models.CharField(max_length=10)),
                ("interval", models.CharField(max_length=8)),
                ("currency", models.CharField(max_length=3)),
                ("rf", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                "ordering": ("-period",),
                "unique_together": {("period", "interval", "currency")},
            },
        ),
        migrations.CreateModel(
            name="FiveSixFactor",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("period", models.CharField(max_length=10)),
                ("interval", models.CharField(max_length=8)),
                ("currency", models.CharField(max_length=3)),
                ("region", models.CharField(max_length=21)),
                (
                    "mktrf",
                    models.DecimalField(decimal_places=8, max_digits=10, null=True),
                ),
                ("smb", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("hml", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("rmw", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("cma", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("mom", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                "ordering": ("-period",),
                "unique_together": {("period", "interval", "currency", "region")},
            },
        ),
        migrations.CreateModel(
            name="ExchangeRateUSDPerX",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("period", models.CharField(max_length=10)),
                ("interval", models.CharField(max_length=8)),
                ("EUR", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("JPY", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("GBP", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("CHF", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("RUB", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("AUD", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("BRL", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("CAD", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("CNY", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("INR", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("DKK", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("NZD", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("NOK", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("SEK", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("PLN", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("ILS", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("KRW", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
                ("TRY", models.DecimalField(decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                "ordering": ("-period",),
                "unique_together": {("period", "interval")},
            },
        ),
    ]
