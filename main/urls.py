from django.urls import path
from main import views
App_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('download', views.download_file, name="download")
]
