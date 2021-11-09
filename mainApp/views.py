from django.shortcuts import render

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

