from webbrowser import get
from django.contrib import admin
from django.urls import path
from patient.views import get, patient_detail_view
from patient.views import list_venues
from patient.views import show_angio



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', patient_detail_view),
    path('angio/',list_venues ),
    path('show_angio/<sudo_id>', show_angio, name='show-angio'),
    path('home/', get),
   
   
]
