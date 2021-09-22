from django.db import models

# Create your models here.

class Propietario(models.Model):
    idpropietario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=60)
    comentarios = models.TextField(blank=True)
    class Meta:
        db_table = 'propietario'
class Tipo_mascota(models.Model):
    idtipo_mascota = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    class Meta:
        db_table = 'tipo_mascota'
class Mascota(models.Model):
    idmascota = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    tipo_mascota = models.ForeignKey(Tipo_mascota, on_delete=models.SET_NULL, null=True, db_column='tipo_mascota')
    propietario = models.ForeignKey(Propietario, on_delete=models.SET_NULL, blank=True, null=True, db_column='propietario')
    class Meta:
        db_table = 'mascota'