from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class PPL(models.Model):
    nui = models.IntegerField()
    n_td = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha_nacimiento = models.DateField()
    fecha_captura = models.DateField()
    situacion_juridica = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    ubicacion = models.CharField(max_length=50)
    delito = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Area(models.Model):
    nombre_area = models.CharField(max_length=50)
    descripcion_area = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tipo_tramite (models.Model):
    id_area= models.ForeignKey(Area,on_delete=models.CASCADE)
    descripcion_tipo = models.CharField(max_length=200,null=True,blank=True)
    nombre_tipo = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    



class Estado_tramites(models.Model):
    estado_tramite = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Funcionario(models.Model):
    id_area=models.ForeignKey(Area,on_delete=models.CASCADE)
    documento_funci = models.IntegerField()
    nombre_funci = models.CharField(max_length=50)
    apellidos_funci = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    genero_funci = models.CharField(max_length=10)
    passw = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    



class Prestamo_hv (models.Model):
    id_ppl = models.ForeignKey(PPL,on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    


class PPLxTramites(models.Model):
    id_ppl = models.ForeignKey(PPL,on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    id_tipotramite = models.ForeignKey(Tipo_tramite,on_delete=models.CASCADE)
    id_estadotramite = models.ForeignKey(Estado_tramites,on_delete=models.CASCADE)
    fecha_peticion = models.DateField()
    fase_72h = models.CharField(max_length=100,null=True,blank=True)
    visitadomi_72h = models.CharField(max_length=100,null=True,blank=True)
    antecedentes_72h = models.CharField(max_length=100,null=True,blank=True)
    radi_oficio_libertades = models.IntegerField(null=True,blank=True)
    autoridad_tutela = models.CharField(max_length=100,null=True,blank=True)
    asunto_tutela = models.CharField(max_length=100,null=True,blank=True)
    oficio_envio_tutela = models.CharField(max_length=100,null=True,blank=True)
    observa_desa_tutela = models.CharField(max_length=200,null=True,blank=True)
    observaciones = models.CharField(max_length=200,null=True,blank=True)
    fecha_envio_tramite= models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)




