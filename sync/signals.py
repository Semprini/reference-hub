from django.db.models.signals import post_save, post_delete

from .models import CanonicalSource, CanonicalUpdate, Destination, RDBMSInstance, UpdateJob
from .serializers import CanonicalSourceSerializer, CanonicalUpdateSerializer, DestinationSerializer, RDBMSInstanceSerializer, UpdateJobSerializer


def run_update(sender, instance, **kwargs):
    canonical_source = instance.canonical_source
    for job in canonical_source.update_jobs.all():
        print(f"{job.table_name}")
        print(f"UPDATE {job.table_name} SET {job.destination_fields} = '{instance.json[job.canonical_fields]}' WHERE {job.where_clause}")


def init_signals():
    post_save.connect(run_update, sender=CanonicalUpdate)
