from django import forms

from .models import Cita, Medico, User, Lugar_Nacimiento, Persona

class PersonaForms(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ( 'dni', 'nombres', 'apellido_paterno','apellido_materno','sexo',
                   'fecha_nacimiento', 'grado_instruccion','lugar_nacimiento', 'telefono', 
                   'edad', 'correo', 'nacionalidad','ocupacion', 'domicilio', 'centro_trabajo','direccion_laboral',
                   'numero_Seguro', 'nombres_apellidos_Padre' , 'nombres_apellidos_Madre', 'contacto_urgencia',
                   'dirección_contacto','parentesco','tipo_Seguro'  ,'estado_civi' ,'estado_padre' , 
                   'estado_madre' ,'diagnostico', )
        labels = {
                'dni':'DNI', 'nombres':'Nombres', 'apellido_paterno':'Apellido Paterno',
                'apellido_materno':'Apellido Materno', 'fecha_nacimiento':'Fecha Nacimiento: AÑO-MES-DIA', 
                'correo':'Correo', 'telefono':'Telefono','edad':'Edad', 'diagnostico':'Diagnostico',
                'nacionalidad':'Nacionalidad', 'grado_instruccion':'Grado Instruccion', 'ocupacion': 'Ocupacion',
                'domicilio':'Domicilio', 'centro_trabajo':'Centro Trabajo' ,  'direccion_laboral':'Direccion del Trabajo',
                'numero_Seguro': 'Número del Seguro', 'nombres_apellidos_Padre':'Nombre y Apellidos del Padre',
                'nombres_apellidos_Madre':'Nombre y Apellidos de la Madre', 'contacto_urgencia':'Contacto de Urgencias',
                'dirección_contacto':'Dirección de Contacto', 'parentesco': 'Parentesco', 'estado_padre':'Estado del Padre',
                'estado_madre':'Estado de la madre'}
        
        def __init__(self, *args, **kwargs):
            super(MedicoForms, self).__init__(*args, **kwargs)
            self.fields['tipo_Seguro'].empty_label = "Select"
            self.fields['lugar_nacimiento'].empty_label = "Select"
            self.fields['sexo'].empty_label = "Select"
            self.fields['estado_civi'].empty_label = "Select"  

class MedicoForms(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('dni_Medico', 'nombres_medico','apeliido_paterno_medico', 
                  'apeliido_materno_medico','colegiatura_medico', 'tipo_medico')       
        labels = {
            'dni_Medico': "Dni del Medico:",
            'nombres_medico': 'Nombre del Medico',
            'apeliido_paterno_medico': 'Apellido Paterno',
            'apeliido_materno_medico': 'Apellido Materno',
            'colegiatura_medico': 'Colegiatura del Medico',
            #'id': 'id_medico',      
        }
        def __init__(self, *args, **kwargs):
            super(MedicoForms, self).__init__(*args, **kwargs)
            self.fields['tipo_medico'].empty_label = "Select"
 
class Lugar_NacimientoForm(forms.ModelForm):
    class Meta:
        model = Lugar_Nacimiento
        fields = ('ubigeo', 'distrito','provincia','departamento')
        labels = {'ubigeo': 'Ubicación' }  
        def __init__(self):
            super(Lugar_NacimientoForm, self).__init__()
            self.fields['distrito'].empty_label = "Select"    
            self.fields['provincia'].empty_label = "Select" 
            self.fields['departamento'].empty_label = "Select"  


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ( 'dni', 'nombres', 'apellido_paterno','apellido_materno','sexo',
                   'fecha_nacimiento', 'grado_instruccion','lugar_nacimiento', 'telefono', 
                   'edad', 'correo', 'nacionalidad','ocupacion', 'domicilio', 'centro_trabajo','direccion_laboral',
                   'numero_Seguro', 'nombres_apellidos_Padre' , 'nombres_apellidos_Madre', 'contacto_urgencia',
                   'dirección_contacto','parentesco','tipo_Seguro'  ,'estado_civi' ,'estado_padre' , 
                   'estado_madre' ,'diagnostico', )
        labels = {
                'dni':'DNI', 'nombres':'Nombres', 'apellido_paterno':'Apellido Paterno',
                'apellido_materno':'Apellido Materno', 'fecha_nacimiento':'Fecha Nacimiento: AÑO-MES-DIA', 
                'correo':'Correo', 'telefono':'Telefono','edad':'Edad', 'diagnostico':'Diagnostico',
                'nacionalidad':'Nacionalidad', 'grado_instruccion':'Grado Instruccion', 'ocupacion': 'Ocupacion',
                'domicilio':'Domicilio', 'centro_trabajo':'Centro Trabajo' ,  'direccion_laboral':'Direccion del Trabajo',
                'numero_Seguro': 'Número del Seguro', 'nombres_apellidos_Padre':'Nombre y Apellidos del Padre',
                'nombres_apellidos_Madre':'Nombre y Apellidos de la Madre', 'contacto_urgencia':'Contacto de Urgencias',
                'dirección_contacto':'Dirección de Contacto', 'parentesco': 'Parentesco', 'estado_padre':'Estado del Padre',
                'estado_madre':'Estado de la madre'}
        
        def __init__(self, *args, **kwargs):
            super(MedicoForms, self).__init__(*args, **kwargs)
            self.fields['tipo_Seguro'] = "Select"
            self.fields['lugar_nacimiento'] = "Select"
            self.fields['sexo'] = "Select"
            self.fields['estado_civi'] = "Select"  
        
        def __str__(self):
          return self.descripcion_sexo