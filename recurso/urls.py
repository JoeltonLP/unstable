from django.urls import path

from .views import teacher_index


urlpatterns = [
    path('professores', teacher_index)
]