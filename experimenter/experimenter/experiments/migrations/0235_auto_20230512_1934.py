# Generated by Django 3.2.19 on 2023-05-12 19:34

from django.db import migrations


def remove_dirty_publish_status(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusExperiment.objects.filter(publish_status="Dirty").update(
        publish_status="Idle", is_rollout_dirty=True
    )


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0234_alter_nimbusexperiment_is_rollout_dirty"),
    ]

    operations = [
        migrations.RunPython(remove_dirty_publish_status),
    ]