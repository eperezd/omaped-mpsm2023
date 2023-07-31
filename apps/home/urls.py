from django.urls import path, re_path
from apps.home import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('index.html', views.dashboard, name='index'),
    path('persona_forms.html', views.Personas_Forms, name='Personas_Forms'),
    path('lista.html', views.lista, name='lista'),    

    path('prueba.html', views.prueba, name='prueba'),

    path('medico_forms', views.Medico_Forms, name='Medico_Forms'),
    path('medicos.html', views.medicos, name='medicos'),

    path('base_modificar/<int:id>', views.Editar_Forms, name='Editar_Forms'),

    path('edicionPersona/<int:id>', views.edicionPersona),
    path('editarPersona/', views.editarPersona),
    path('ReposrtePDF/<int:id>', views.ReposrtePDF, name='ReposrtePDF'), 

    path('Trabajadores', views.Trabajadores, name='Trabajadores'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
