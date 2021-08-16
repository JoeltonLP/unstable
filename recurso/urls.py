from django.urls import path

from .views import (
    professor_index,
    professor_by_id,
    recurso_index,
    recurso_by_id,
    recurso_data_show_index,
    recurso_data_show_by_id,
    agendamento_index,
    agendamento_by_id,
    get_log_index,
    get_log_by_id
)


urlpatterns = [
    path('professor', professor_index),
    path('professor/<int:id>', professor_by_id),
    path('recurso', recurso_index), 
    path('recurso/<int:id>', recurso_by_id),
    path('recurso-data-show', recurso_data_show_index), 
    path('recurso-data-show/<int:id>', recurso_data_show_by_id),
    path('agendamento', agendamento_index), 
    path('agendamento/<int:id>', agendamento_by_id), 
    path('log', get_log_index), 
    path('log/<int:id>', get_log_by_id)
]