from django.urls import path

from .views import (
    professor_get_index,
    professor_index_by_pk,
    recurso_get_index,
    recurso_index_by_pk,
    agendamento_get_index,
    agendamento_index_by_pk  
)


urlpatterns = [
    path('professor', professor_get_index),
    path('professor/<int:pk>', professor_index_by_pk),
    path('recurso', recurso_get_index), 
    path('recurso/<int:pk>', recurso_index_by_pk),
    path('agendamento', agendamento_get_index), 
    path('agendamento/<int:pk>', agendamento_index_by_pk)
]