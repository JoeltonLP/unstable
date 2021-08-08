from .serealizers import (
    TeacherSerializer, 
    ResourceSerializer, 
    LoanResourceSerealizer
)

from helpers import restfy


professores_get_index, professor_index_by_pk = restfy.make_rest(TeacherSerializer)
recursos_get_index, recurso_index_by_pk = restfy.make_rest(ResourceSerializer)
reservas_get_index, reserva_index_by_pk = restfy.make_rest(LoanResourceSerealizer)