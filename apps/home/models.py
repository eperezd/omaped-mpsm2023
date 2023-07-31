# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
#from .choices import sexos, civil, seguro, estados_padres

class Lugar_Nacimiento(models.Model):
    id = models.AutoField(primary_key=True)
    ubigeo = models.CharField(max_length=6, verbose_name='Ubigeo')
    distrito = models.CharField(max_length=20 , verbose_name='Distrito')
    provincia = models.CharField(max_length=20, verbose_name='Provincia')   
    departamento = models.CharField(max_length=20, verbose_name='Departamento') 
    
    def __str__(self):
          return self.ubigeo
    
    class Meta:
            verbose_name = 'Lugar_Nacimiento'
            verbose_name_plural = 'Lugar_Nacimiento'    
            db_table = 'Lugar_Nacimiento'
            ordering = ['ubigeo', '-distrito']  

class Sexos(models.Model):
     id = models.AutoField(primary_key=True)    
     descripcion_sexo = models.CharField(max_length=10, verbose_name='Sexo') 
     estado_sexo = models.BooleanField(verbose_name='Condicion')

     def __str__(self):
          return self.descripcion_sexo  

     class Meta:
          verbose_name = 'Sexo' 
          verbose_name_plural = 'Sexos'
          db_table = 'Sexos'
          ordering = ['descripcion_sexo']

class Estado_Civil(models.Model):
     id = models.AutoField(primary_key=True)    
     descripcion_estado_civil = models.CharField(max_length=10, verbose_name='Estado Civil')
     condicion_estado_civil = models.BooleanField(verbose_name='Condicion')

     def __str__(self):
          return self.descripcion_estado_civil
     
     class Meta:
          verbose_name = 'Estado Civil' 
          verbose_name_plural = 'Estado Civil'
          db_table = 'Estado_Civil'   
          ordering = ['descripcion_estado_civil']   

class Seguro(models.Model): 
     id = models.AutoField(primary_key=True)
     descripcion_seguro = models.CharField(max_length=10, verbose_name='Tipo de Seguro')
     abreviatura_seguro = models.CharField(max_length=10, verbose_name='Abreviatura')                                           
     estado_seguro = models.BooleanField(verbose_name='Estado seguro')
     
     def __str__(self): 
          return self.descripcion_seguro
     
     class Meta:
          verbose_name = 'Tipo de Seguro'
          verbose_name_plural = 'Tipo de Seguro'
          db_table = 'Seguro'
          ordering = ['descripcion_seguro']

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8 , verbose_name='dni')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    fecha_nacimiento = models.CharField(max_length=20,verbose_name='Fecha de Nacimiento')
    correo = models.EmailField(verbose_name='Correo')   
    telefono = models.CharField(max_length=11, verbose_name='Telefono') 
    edad = models.IntegerField(verbose_name='Edad')
    diagnostico = models.TextField(max_length=600, verbose_name='Diagnostico')
    nacionalidad = models.CharField(max_length=20,verbose_name='Nacionalidad')
    grado_instruccion = models.CharField(max_length=20, verbose_name='Grado de Instrucción')
    ocupacion = models.CharField(max_length=20, verbose_name='ocupacion')
    domicilio = models.CharField(max_length=30, verbose_name='Domicilio')
    centro_trabajo = models.CharField(max_length=20, verbose_name='Centro de Trabajo')
    direccion_laboral = models.CharField(max_length=30, verbose_name='Dirección del trabajo')
    numero_Seguro= models.CharField(max_length=20, verbose_name='Número de seguro')
    nombres_apellidos_Padre = models.CharField(max_length=20, verbose_name='Nombres de padre')
    nombres_apellidos_Madre	= models.CharField(max_length=20, verbose_name='Nombres de la Madre')
    contacto_urgencia = models.CharField(max_length=20, verbose_name='Nombre de Contacto')
    dirección_contacto = models.CharField(max_length=20, verbose_name='Dirección de Contacto')
    parentesco = models.CharField(max_length=20, verbose_name='Parentesco')
    tipo_Seguro = models.ForeignKey(Seguro, null=True, blank=True,on_delete=models.CASCADE)
    lugar_nacimiento = models.ForeignKey(Lugar_Nacimiento, null=True, blank=True,on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexos, null=True, blank=True,on_delete=models.CASCADE)
    estado_civi = models.ForeignKey(Estado_Civil, null=True, blank=True,on_delete=models.CASCADE)
    #lugar_nacimiento = models.ForeignKey(Lugar_Nacimiento, null=True, blank=True,on_delete=models.CASCADE)
    estado_padre = models.CharField(max_length=10 ,verbose_name='Estado padre')
    estado_madre = models.CharField(max_length=10 ,verbose_name='Estado madre')




    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
            verbose_name = 'Persona'
            verbose_name_plural = 'Personas'    
            db_table = 'Persona'
            ordering = ['id', '-apellido_materno']  
  
      
class Cita(models.Model):
    id_citas = models.AutoField(primary_key=True)
    fecha_cita = models.CharField(max_length=15, verbose_name='Fecha de cita')
    hora_cita = models.TimeField(verbose_name='Hora de cita')   
    lugar_cita = models.CharField(max_length=20, verbose_name='Lugar')
    class Meta:
            verbose_name = 'Cita'
            verbose_name_plural = 'Citas'    
            db_table = 'Cita'
            ordering = ['id_citas']  

class Tipo_Medico(models.Model):
     id = models.AutoField(primary_key=True)    
     descripcion_tipo_medico = models.CharField(max_length=20, verbose_name='Tipo Medico')
     estado_tipo_medico = models.BooleanField(default=False, verbose_name='Estado Medico')
     
     def __str__(self):
          return self.descripcion_tipo_medico
     
     class Meta:
          verbose_name = 'Tipo de Medico'   
          verbose_name_plural = 'Tipo de Medico'
          db_table = 'Tipo_Medico'
          ordering = ['descripcion_tipo_medico']    


class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    dni_Medico = models.IntegerField(verbose_name='Id_Medico')
    nombres_medico = models.CharField(max_length=20, verbose_name='Nombre Medico')
    apeliido_paterno_medico = models.CharField(max_length=20, verbose_name='Nombre Medico')
    apeliido_materno_medico = models.CharField(max_length=20, verbose_name='Nombre Medico')
    colegiatura_medico = models.CharField(max_length=20, verbose_name='Colegiatura Medico')
    tipo_medico = models.ForeignKey(Tipo_Medico, null=True, blank=True,on_delete=models.CASCADE)    

    def nombre_completo(self):
        return "{} {}, {}".format(self.apeliido_paterno_medico, self.apeliido_materno_medico, self.nombres_medico)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
            verbose_name = 'Medico'
            verbose_name_plural = 'Medicos'    
            db_table = 'Medico'
            ordering = ['id', '-id']  

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    dni_personal = models.IntegerField(verbose_name='DNI')
    nombres_personal = models.CharField(max_length=20, verbose_name='Nombre de personal')
    apellido_paterno_personal = models.CharField(max_length=20, verbose_name='Apellido Paterno')    
    apellido_materno_personal = models.CharField(max_length=20, verbose_name='Apellido Materno')
    
    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno_personal, self.apellido_materno_personal, self.nombres_personal)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
            verbose_name = 'Personal'
            verbose_name_plural = 'Personals'    
            db_table = 'Personal'
            ordering = ['apellido_paterno_personal', '-apellido_materno_personal']  

class Detalle_Cita(models.Model):
    id = models.AutoField(primary_key=True)
    asistencia= models.BooleanField(default='0')
    observaciones = models.TextField(max_length=20, verbose_name='Observaciones')  
    persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)  
    id_Citas = models.ForeignKey(Cita, null=True, blank=True,on_delete=models.CASCADE)
    dni_medico = models.ForeignKey(Medico,null=True, blank=True,on_delete=models.CASCADE)
    Personal = models.ForeignKey(Personal,null=True, blank=True , on_delete=models.CASCADE)
    class Meta:
            verbose_name = 'Detalle_Cita'
            verbose_name_plural = 'Detalle_Citas'    
            db_table = 'Detalle_Cita'
            ordering = ['id']  

class Certificado(models.Model):
    numero_certificado = models.AutoField(primary_key=True, verbose_name='Numero de Certificado')
    fecha_certificado = models.DateField(verbose_name='Fecha de Certificado')   
    medico_certificado = models.ForeignKey(Medico, null=True, blank=True,on_delete=models.CASCADE) 
    personal_cetificado = models.ForeignKey(Personal, null=True, blank=True,on_delete=models.CASCADE) 
    estado_certificado = models.BooleanField(verbose_name='Estado')
    dni_persona = models.ForeignKey(Persona, null=True, blank=True,on_delete=models.CASCADE)
    
    class Meta:
            verbose_name = 'Certificado'
            verbose_name_plural = 'Certificados'    
            db_table = 'Certificado'
            ordering = ['numero_certificado']  

   

