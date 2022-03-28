from pyexpat import model
from .models import Domicilio
from DomiCercaBackend.serializers import AuditSerializer

class DomiciloSerializers(AuditSerializer):
    class Meta(AuditSerializer.Meta):
        model = Domicilio
        read_only_fields = ('active',)