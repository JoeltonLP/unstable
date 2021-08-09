from .serealizers import (
    TeacherSerializer, 
    ResourceSerializer, 
    LoanResourceSerealizer
)

from helpers import restfy


professor_get_index, professor_index_by_pk = restfy.make_rest(TeacherSerializer)
recurso_get_index, recurso_index_by_pk = restfy.make_rest(ResourceSerializer)
agendamento_get_index, agendamento_index_by_pk = restfy.make_rest(LoanResourceSerealizer)