
from django.urls import path
from .views import pacientes_list
from .views import pacientes_new
from .views import pacientes_update
from .views import pacientes_delete

urlpatterns = [
    path('list/', pacientes_list, name="pacientes_list"),
    path('new/', pacientes_new, name="pacientes_new"),
    path('update/<int:id>/', pacientes_update, name="pacientes_update"),
    path('delete/<int:id>/', pacientes_delete, name="pacientes_delete")
]
