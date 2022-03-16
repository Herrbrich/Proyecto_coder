from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def primer_vista(request):
    return HttpResponse("Hola  mundo desde mi primer vista de Django")

def second_vista(request):
    return HttpResponse("<h1>Titulo  1</h1> <p>Esto es un parrafo </p>") 

def dia_hora(recuest):
    fecha_hora = datetime.now()
    return HttpResponse(f"<p>Tiempo actual: {fecha_hora}</p>")

def nombre_usuario(request, nombre):
    return HttpResponse(F"Tu nombre es {nombre}")

def edad_usuario(request, edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse(F"Usted Nacio en {anio_nacimiento}")

def pagina_inicio(request):
    archivo = open(r"C:\Users\Compumar\Documents\django-intro\proyecto_coder\proyecto_coder\templates\page.html", 'r')
    plantilla = Template(archivo.read())

    archivo.close()

    context = Context()

    documento = plantilla.render(context)
    
    return HttpResponse(documento) 