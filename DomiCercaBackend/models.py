from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Creado el', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado el', auto_now=True)

    class Meta:
        abstract = True


class AuditModel(BaseModel):
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', verbose_name='Creado por',
                                   on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
