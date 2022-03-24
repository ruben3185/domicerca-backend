from pyexpat import model
from django.db import models
from DomiCercaBackend.models import AuditModel
from DomiCercaBackend.defs import media_upload_to


class Domicilio(AuditModel):
    correo = models.EmailField("Correo")
    nombre = models.CharField(max_length=500)
    latitud = models.CharField("latitud", max_length=500)
    longitud = models.CharField("logitud", max_length=500)
    imagen = models.ImageField(("iamgen"), upload_to=media_upload_to, height_field=None, width_field=None, max_length=None,  null=True, blank=True,)
    telefono = models.IntegerField("Telefono")
    
    def __int__ (self):
        return self.id

    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

