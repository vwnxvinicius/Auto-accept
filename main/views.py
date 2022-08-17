from django.http import HttpResponse
from django.shortcuts import render
# Clicker functions
from clicker import string_separator, accept_match

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
        resolution_x = string_separator(resolution, 1)
        resolution_y = string_separator(resolution, 0)
        accept_match(int(resolution_x), int(resolution_y))
        return render(request, 'main/clicker.html', 
        {
            'resolution':resolution,
            'resolution_x':resolution_x,
            'resolution_y':resolution_y,
        }
        )