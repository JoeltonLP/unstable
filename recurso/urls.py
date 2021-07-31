from django.urls import path

from .views import (
    professores_get_index,
    professores_index_by_pk 
)


urlpatterns = [
    path('professores', professores_get_index),
    path('professores/<int:pk>', professores_index_by_pk),
    # path('agendamento', get_index), 
    # path('agendamento<int:pk>', index_by_pk)
]