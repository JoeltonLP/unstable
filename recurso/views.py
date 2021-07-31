from .models import Teacher, Resource
from .serealization import TeacherSerializer, ResourceSerializer

from .rest.rest import make_rest


professores_get_index, professor_index_by_pk = make_rest(Teacher, TeacherSerializer)
recursos_get_index, recurso_index_by_pk = make_rest(Resource, ResourceSerializer)
