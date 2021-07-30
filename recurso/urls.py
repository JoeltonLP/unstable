from django.urls import path

from .views import (
    index,
    index_by_pk, 
)


urlpatterns = [
    path('professores', index),
    path('professores/<int:pk>', index_by_pk),
    path('agendamento', index), 
    path('agendamento<int:pk>', index_by_pk)
]