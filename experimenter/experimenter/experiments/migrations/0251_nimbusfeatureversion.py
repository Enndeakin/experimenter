# Generated by Django 3.2.23 on 2023-11-22 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0250_nimbusexperiment_qa_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="NimbusFeatureVersion",
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
                ("major", models.IntegerField()),
                ("minor", models.IntegerField()),
                ("patch", models.IntegerField()),
            ],
            options={
                "verbose_name": "Nimbus Feature Version",
                "verbose_name_plural": "Nimbus Feature Versions",
                "unique_together": {("major", "minor", "patch")},
            },
        ),
        migrations.AlterField(
            model_name="nimbusversionedschema",
            name="version",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="experiments.nimbusfeatureversion",
            ),
        ),
    ]