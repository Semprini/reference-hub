from django.utils.translation import gettext_lazy as _
from django.db import models
from simple_history.models import HistoricalRecords

from EncryptedCharField import EncryptedCharField


class ENUM_RDBMSType(models.TextChoices):
    ORACLE = 'Oracle', _('Oracle')
    DB2 = 'DB2', _('DB2')
    POSTGRES = 'Postgres', _('Postgres')

class ENUM_UpdateStatus(models.TextChoices):
    IN_PROGRESS = 'In Progress', _('In Progress')
    COMPLETED = 'Completed', _('Completed')
    FAILED = 'Failed', _('Failed')


class Destination( models.Model ):
    id = models.AutoField( primary_key=True,  )
    name = models.CharField( blank=True, null=True, max_length=100 )

    class Meta:
        abstract = True


class CanonicalSource( models.Model ):
    name = models.CharField( blank=True, null=True, max_length=100 )
    id = models.AutoField( primary_key=True,  )

    def __str__(self):
        return self.name


class CanonicalUpdate( models.Model ):
    json = models.JSONField( blank=True, null=True,  )
    id = models.AutoField( primary_key=True,  )
    update_time = models.DateTimeField( blank=True, null=True, auto_now=True )
    status = models.CharField( max_length=100, choices=ENUM_UpdateStatus.choices, blank=True, null=True )
    canonical_source = models.ForeignKey( 'sync.CanonicalSource', related_name='canonical_updates', on_delete=models.CASCADE, blank=True, null=True )
    
    def __str__(self):
        return f"{self.update_time} | {self.canonical_source.name}"


class RDBMSInstance( Destination ):
    rdbms_type = models.CharField( max_length=100, choices=ENUM_RDBMSType.choices, blank=True, null=True )
    secret = EncryptedCharField( blank=True, null=True, max_length=256 )
    connection_string = models.CharField( blank=True, null=True, max_length=100 )
    history = HistoricalRecords()


    def __str__(self):
        return self.name


class UpdateJob( models.Model ):
    id = models.AutoField( primary_key=True,  )
    table_name = models.CharField( blank=True, null=True, max_length=100 )
    canonical_fields = models.CharField( blank=True, null=True, max_length=100 )
    destination_fields = models.CharField( blank=True, null=True, max_length=100 )
    where_clause = models.CharField( blank=True, null=True, max_length=100 )
    canonical_source = models.ForeignKey( 'sync.CanonicalSource', related_name='update_jobs', on_delete=models.CASCADE, blank=True, null=True )
    rdbms_instance = models.ForeignKey( 'sync.RDBMSInstance', related_name='update_jobs', on_delete=models.CASCADE, blank=True, null=True )

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.table_name}"

