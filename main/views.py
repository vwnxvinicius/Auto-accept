from urllib import response
from django.shortcuts import render
import mimetypes
import os
from django.http.response import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'mysetup.exe'
    filepath = BASE_DIR + '/main/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response