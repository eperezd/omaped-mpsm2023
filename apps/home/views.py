import csv
from msilib.schema import ListView
from django.views.generic import ListView
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from apps.home.forms import MedicoForms, PersonaForms, ReporteForm
from apps.home.models import Persona, Medico, Personal
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import (
        Paragraph, 
        Table, 
        SimpleDocTemplate, 
        Spacer, 
        TableStyle, 
        Paragraph)
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.db.models import Q
from django.conf import settings

from apps.home.utils import render_to_pdf


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/map.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def dashboard(request):
    personas = Persona.objects.all()
    total = personas.count()
    return render(request, 'home/index.html' , {'personas': personas, 'total': total})

def lista(request):
    busqueda = request.POST.get("buscar")
    personas = Persona.objects.all()

    if busqueda:
        personas = Persona.objects.filter(
            Q(dni__icontains = busqueda) | 
            Q(nombres__icontains = busqueda) |
            Q(apellido_paterno__icontains = busqueda) |
            Q(apellido_materno__icontains = busqueda)
        ).distinct()

    return render(request, 'home/prueba.html',{'personas': personas})  

def prueba(request):
    busqueda = request.POST.get("buscar")
    personas = Persona.objects.all()

    if busqueda:
        personas = Persona.objects.filter(
            Q(dni__icontains = busqueda) | 
            Q(nombres__icontains = busqueda) |
            Q(apellido_paterno__icontains = busqueda) |
            Q(apellido_materno__icontains = busqueda)
        ).distinct()

    return render(request, 'home/prueba.html',{'personas': personas})  

def medicos(requests):
    medicos= Medico.objects.all()
    return render(requests, 'home/medicos.html', {'medicos': medicos})   

def Medico_Forms(request):
    if request.method == "GET":
        formmedicos = MedicoForms()
        return render(request, 'home/medico_forms.html',{'formmedicos':formmedicos})    
    else:
        formmedicos = MedicoForms(request.POST)
        if formmedicos.is_valid():
            formmedicos.save()
        return redirect('medicos')  
 
def Personas_Forms(request):
    if request.method == "GET":
        form_personas = PersonaForms()
        return render(request, 'home/persona_forms.html',{'form_personas':form_personas})    
    else:
        form_personas = PersonaForms(request.POST)
        if form_personas.is_valid():
            form_personas.save()
        return redirect('lista')  

def Editar_Forms(request, id):
    persona = Persona.objects.get(id=id)
    formulario = ReporteForm(request.POST or None,instance=persona) 
    if formulario.is_valid():   
       formulario.save()
       return redirect('lista')
    return render(request, 'home/base_modificar.html',{'formulario':formulario})    

def Reportes(request, id):
    # Crear el objeto HttpResponse con sus cabeceras
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte.csv"'
    # Se usa el response como un "archivo" destino
    writer = csv.writer(response)
    # Obtener los objetos que deseas exportar e iterar
    objetos = Persona.objects.all()
    for objeto in objetos:
        row = [
            objeto.dni,
            objeto.nombres,
            objeto.apellido_materno
        ]
        writer.writerow(row)
    return response

def edicionPersona(request, id):
    personas = Persona.objects.get(id=id)
    return render(request, 'home/edicionPersona.html', {'personas':personas})

def editarPersona(request):
    id = request.POST["textId"]
    dni = request.POST['textDni']
    nombres = request.POST["textNombres"]
    apellido_paterno = request.POST['textApellidoPaterno']
    apellido_materno = request.POST['textApellidoMaterno']
    fecha_nacimiento = request.POST['textFechaNacimiento']
    correo = request.POST['textEmail']
    telefono = request.POST['textTelefono']
    edad = request.POST['textEdad']
    diagnostico = request.POST['textDiagnostico']
    nacionalidad = request.POST['textNacionalidad']
    grado_instruccion = request.POST['textGradoInstruccion'] 
    ocupacion = request.POST['textOcupacion'] 
    domicilio = request.POST['textDomicilio'] 
    centro_trabajo = request.POST['textCentroTrabajo'] 
    direccion_laboral = request.POST['textDomicilioTrabajo'] 
    numero_Seguro = request.POST['textNumeroSeguro'] 
    nombres_apellidos_Padre = request.POST['texDatosPadre'] 
    nombres_apellidos_Madre = request.POST['texDatosMadre'] 
    contacto_urgencia = request.POST['textTelefonoParentesco'] 
    dirección_contacto = request.POST['textDireccionParentesco'] 
    parentesco = request.POST['textParentescoContacto'] 
    tipo_Seguro = request.POST['textTipoSeguro']  
    lugar_nacimiento = request.POST['textLugarNacimiento']  
    sexo = request.POST['textSexo']   
    estado_civi = request.POST['textEstadoCivil']  
    estado_padre = request.POST['textEstadoPadre']  
    estado_madre = request.POST['textEstadoMadre']  
    
    personas = Persona.objects.get(id=id)    
    personas.dni = dni
    personas.nombres = nombres
    personas.apellido_paterno = apellido_paterno
    personas.apellido_materno = apellido_materno 
    personas.fecha_nacimiento = fecha_nacimiento
    personas.correo = correo
    personas.telefono = telefono 
    personas.edad = edad 
    personas.diagnostico = diagnostico
    personas.nacionalidad = nacionalidad
    personas.grado_instruccion = grado_instruccion
    personas.ocupacion = ocupacion
    personas.domicilio = domicilio   
    personas.centro_trabajo = centro_trabajo
    personas.direccion_laboral=direccion_laboral
    personas.numero_Seguro = numero_Seguro
    personas.nombres_apellidos_Padre = nombres_apellidos_Padre
    personas.nombres_apellidos_Madre = nombres_apellidos_Madre
    personas.contacto_urgencia = contacto_urgencia
    personas.dirección_contacto = dirección_contacto
    personas.parentesco = parentesco
    personas.tipo_Seguro = tipo_Seguro   
    personas.lugar_nacimiento=lugar_nacimiento
    personas.sexo = sexo
    personas.estado_civi = estado_civi
    personas.estado_padre = estado_padre
    personas.estado_madre = estado_madre
    personas.save()
    return redirect('home/lista.html')#, {'formulario': formulario})   

def ReposrtePDF(request,id):
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = 'apps/static/assets/img/brand/omaped.jpg' 
       
        #C:\Users\EvenRonald\omaped4\omaped\apps\static\assets\img\brand\omaped.jpg
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="personas.pdf"'
        pdf.drawImage(archivo_imagen, 40, 720, 120, 90,preserveAspectRatio=True)    

        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(150, 790, u"Municipalidad Provincial de San Martin")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE PERSONAS")            
        
        personaslistadas = Persona.objects.get(id=id)
        cabeza1= ('DNI', 'Nombres', 'Apellido Paterno','Apellido Materno')
        seleccion1= [(personaslistadas.dni,personaslistadas.nombres, personaslistadas.apellido_paterno,  
                      personaslistadas.apellido_materno)]
        cabeza2= ( 'Fecha Nac:','Correo', 'Telefono','Edad')
        seleccion2=[(personaslistadas.fecha_nacimiento,personaslistadas.correo,
                     personaslistadas.telefono,personaslistadas.edad)]

        cabeza3=('Domicilio','Sexo', 'Lugar de Nacimiento')
        seleccion3=[(personaslistadas.domicilio,personaslistadas.sexo, 
                     personaslistadas.lugar_nacimiento)]
        
        cabeza4=('Estado Civil','Nacionalidad', 'Grado Instruccion', 'Ocupacion')
        seleccion4=[(personaslistadas.estado_civi,personaslistadas.nacionalidad, 
                     personaslistadas.grado_instruccion,personaslistadas.ocupacion)]

        cabeza5=('Centro Trabajo' , 'Direccion del Trabajo')
        seleccion5=[( personaslistadas.centro_trabajo, personaslistadas.direccion_laboral)]

        cabeza6=('tipo_Seguro', 'Número del Seguro' )
        seleccion6=[(personaslistadas.tipo_Seguro,   personaslistadas.numero_Seguro)]

        cabeza7=('Nombre y Apellidos del Padre','Estado', 'Nombre y Apellidos de la Madre','Estado')
        seleccion7=[(personaslistadas.nombres_apellidos_Padre, personaslistadas.estado_padre,
                     personaslistadas.nombres_apellidos_Madre, personaslistadas.estado_madre
                     )]

        cabeza9=( 'Contacto de Urgencias','Dirección de Contacto','Parentesco')
        seleccion9=[(personaslistadas.parentesco, personaslistadas.contacto_urgencia, personaslistadas.parentesco)]
   
        cabeza8=('Diagnostico',)
        seleccion8=[(personaslistadas.diagnostico, )] 

        detalle1 = Table([cabeza1] + seleccion1, colWidths=[70,130]) 
        detalle1.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle1.wrapOn(pdf, 800, 600)
        detalle1.drawOn(pdf, 50,650)
        
        detalle2 = Table([cabeza2] + seleccion2, colWidths=[70,220,90,80])
        detalle2.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle2.wrapOn(pdf, 800, 600)
        detalle2.drawOn(pdf, 50,600)
        
        detalle3 = Table([cabeza3] + seleccion3, colWidths=[300,60,100])#460 100 180 180
        detalle3.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle3.wrapOn(pdf, 800, 600)
        detalle3.drawOn(pdf, 50,550)

        detalle4 = Table([cabeza4] + seleccion4, colWidths=[70,130])
        detalle4.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle4.wrapOn(pdf, 800, 600)
        detalle4.drawOn(pdf, 50,500)

        detalle5 = Table([cabeza5] + seleccion5, colWidths=[230,230])
        detalle5.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle5.wrapOn(pdf, 800, 600)
        detalle5.drawOn(pdf, 50,450)

        detalle6 = Table([cabeza6] + seleccion6, colWidths=[230,230])
        detalle6.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle6.wrapOn(pdf, 800, 600)
        detalle6.drawOn(pdf, 50,400)

        detalle7 = Table([cabeza7] + seleccion7, colWidths=[180,50,180,50])
        detalle7.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle7.wrapOn(pdf, 800, 600)
        detalle7.drawOn(pdf, 50,350)

        detalle9 = Table([cabeza9] + seleccion9, colWidths=[120,240,100])
        detalle9.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))
        detalle9.wrapOn(pdf, 800, 600)
        detalle9.drawOn(pdf, 50,300)

        detalle8 = Table([cabeza8] + seleccion8, colWidths=[460])
        detalle8.setStyle(TableStyle([('ALIGN',(0,0),(3,0),'LEFT'),('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0, 0), (-1, -1), 10), ]))

        detalle8.wrapOn(pdf, 800, 600)
        detalle8.drawOn(pdf, 50,250)
        texto = '! IMPORTANTE ¡ - Si usted cuenta con algun documento expedido por '
        texto2 = 'un medico especialista o tratante, debe de presentarlo en el momento de la cita'
        texto3 = 'Las Atenciones son en el local del CIAM, Jr. Ricardo Palma cuadra 12 - Tarapoto'
        pdf.drawString(60, 200, texto)
        pdf.drawString(60, 180, texto2)
        pdf.drawString(60, 150, texto3)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

def Trabajadores(request):
    trabajador = Personal.objects.all()
    total = Personal.count()
    return render(request, 'home/listarTrabajador.html' , {'trabajador': trabajador, 'total': total})
