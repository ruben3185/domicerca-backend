from django.contrib import admin

# Register your models here.

from DomiCercaBackend.admin import AuditAdmin
from .models import Domicilio

@admin.register(Domicilio)
class SendEmailPasioloAdmin( AuditAdmin):
    list_display = ('id', 'correo', 'nombre', 'latitud', 'longitud', 'imagen', 'telefono')

