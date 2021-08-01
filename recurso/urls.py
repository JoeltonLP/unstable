from django.urls import path

from .views import (
    professores_get_index,
    professor_index_by_pk,
    recursos_get_index,
    recurso_index_by_pk,
    reservas_get_index,
    reserva_index_by_pk  
)


urlpatterns = [
    path('professores', professores_get_index),
    path('professor/<int:pk>', professor_index_by_pk),
    path('recursos', recursos_get_index), 
    path('recurso/<int:pk>', recurso_index_by_pk),
    path('reservas', reservas_get_index), 
    path('reserva/<int:pk>', reserva_index_by_pk)
]