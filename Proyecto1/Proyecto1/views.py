from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django equipo coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola Mundo!</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Guillermo"
    apellido = "Capdevila"

    namelist = ["Eliane", "Laura", "Ignacio", "Daniel"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    miHtml = open("C:/Users/guill/Clases de Phyton/PyhtonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext = Context(diccionario)
    documento = plantilla.render(miContext)
    return HttpResponse(documento)

    
