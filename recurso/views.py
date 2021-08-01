from .models import (
    Teacher, 
    Resource, 
    LoanResource
)
from .serealization import (
    TeacherSerializer, 
    ResourceSerializer, 
    LoanResourceSerealizer
)

from .rest.rest import make_rest


professores_get_index, professor_index_by_pk = make_rest(Teacher, TeacherSerializer)
recursos_get_index, recurso_index_by_pk = make_rest(Resource, ResourceSerializer)
reservas_get_index, reserva_index_by_pk = make_rest(LoanResource, LoanResourceSerealizer)