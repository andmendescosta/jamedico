
from django.urls import path
from .views import pacientes_list

urlpatterns = [
    path('list/', pacientes_list)
]
