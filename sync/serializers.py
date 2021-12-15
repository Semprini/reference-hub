from rest_framework import serializers
from drf_nest.serializer_fields import TypeField


from .models import CanonicalSource
from .models import CanonicalUpdate
from .models import Destination
from .models import RDBMSInstance
from .models import UpdateJob


class CanonicalSourceSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

	

    class Meta:
        model = CanonicalSource
        fields = ('type', 'url', 
                    'name','id',
					
                    'canonical_updates','update_jobs',
                )

class CanonicalUpdateSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

	

    class Meta:
        model = CanonicalUpdate
        fields = ('type', 'url', 
                    'json','id','update_time','status',
					'canonical_source',
                    
                )

class DestinationSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

	

    class Meta:
        model = Destination
        fields = ('type', 'url', 
                    'id','name',
					
                    
                )

class RDBMSInstanceSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

	

    class Meta:
        model = RDBMSInstance
        fields = ('type', 'url', 
                    'rdbms_type','secret','connection_string','id','name',
					
                    'update_jobs',
                )

class UpdateJobSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

	

    class Meta:
        model = UpdateJob
        fields = ('type', 'url', 
                    'id','table_name','canonical_fields','destination_fields',
					'canonical_source','rdbms_instance',
                    
                )
