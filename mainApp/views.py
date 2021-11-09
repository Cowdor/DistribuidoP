from django.shortcuts import render, HttpResponse
from mainApp.models import Area, Funcionario

# Create your views here.
def archivo(request):
    return render(request, "vista_archivo.html")

def redenciones(request):
    return render(request, "vista_reden.html")

def libertades(request):
    return render(request, "vista_liber.html")

def A_72h(request):
    return render(request, "vista_72h.html")

def tutelas(request):
    return render(request, "vista_tutelas.html")

def index(request):
    return render(request, "index.html")

def asesor(request):
    return render(request, "vista_asesor.html")


def guardar_funci(request):

    funcionario = Funcionario(
        id_area=1,
        documento_funci = 17087678,
        nombre_funci = 'Andrea',
        apellidos_funci = 'Campos',
        cargo = 'Administrador',
        genero_funci = 'Femenino',
        passw = 17087678
    )

    funcionario.save()
    return HttpResponse(f'dato almacenado: {funcionario.nombre_funci}')

def guardar_area(request):

    area = Area(
        nombre_area = 'Tutelas',
        descripcion_area = 'Realizar seguimiento y control de tutelas'

    )

    area.save()
    return HttpResponse(f'dato almacenado: {area.nombre_area}')