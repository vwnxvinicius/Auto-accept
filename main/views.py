from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from webbrowser import get
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def clicker(request):
    try:
        resolution = request.GET['resolution']
    except (KeyError):
        error_message = "Ocorreu um erro inesperado"
        return render(request, 'main/error.html', {error_message: "error_message"})
    else:
        return render(request, 'main/clicker.html', {'resolution':resolution})

'''
def check_values(request):
    try:
        resolution = request.GET['resolution']
    except (KeyError):
        error_message = "Ocorreu um erro inesperado"
        return render(request, 'main/error.html', {error_message: "error_message"})
    else:
        return HttpResponseRedirect(f'/clicker/{resolution}')
'''