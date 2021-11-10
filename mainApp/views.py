from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from mainApp.models import *
from django.contrib import messages


# Create your views here.
def archivo(request):
    ppls = mostrarppls()

    return render(request, "vista_archivo.html",{
        
        'ppls'       :ppls,

    })

def mostrarppls():
    ppls= PPL.objects.all()

    return(ppls)


def guardar_prestamo(request):

    if request.method == 'POST':
        
        
        prestamos = Prestamo_hv(
            
        )

        prestamos.save()
        
        messages.success(request,f"ppl{nui}")
    else:
        messages.error(request,f"no se guardo el ppl")
        
    return redirect("archivo")

def guardar_ppl(request):

    if request.method == 'POST':
        nui = request.POST['nui']
        n_td = request.POST['n_td']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        documento = request.POST['documento']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        fecha_captura = request.POST['fecha_captura']
        situacion_juridica = request.POST['situacion_juridica']
        genero = request.POST['genero']
        ubicacion = request.POST['ubicacion']
        delito = request.POST['delito']
        
        ppl = PPL(
            nui = nui,
            n_td = n_td,
            nombre = nombre,
            apellido = apellido,
            documento = documento,
            fecha_nacimiento = fecha_nacimiento,
            fecha_captura = fecha_captura,
            situacion_juridica = situacion_juridica,
            genero = genero,
            ubicacion = ubicacion,
            delito = delito
        )

        ppl.save()
        
        messages.success(request,f"ppl{nui}")
    else:
        messages.error(request,f"no se guardo el ppl")
        
    return redirect("archivo")


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

def prueba(request):
    return render(request, "prueba.html")


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

def seccion(request):
    if request.method == 'POST':
        documento= request.POST['usuario']
        password = request.POST['pass']
        
        funci_docu = Funcionario.documento_funci,
        funci_pass = Funcionario.passw,
        funci_area = Funcionario.id_area,

        if (documento== funci_docu and password== funci_pass):
            if (funci_area == 1):
                return render(request, "vista_archivo.html")
            elif(funci_area==2):
                return render(request, "vista_72h.html")
            elif(funci_area==3):
                return render(request, "vista_liber.html")
            elif(funci_area==4):
                return render(request, "vista_reden.html")
            elif(funci_area==5):
                return render(request, "vista_tutelas.html")
        else:
            
            return render(request, "index.html")
    else:
        return render(request, "index.html")
    
    return redirect('')


        