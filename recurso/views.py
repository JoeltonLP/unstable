from .models import Teacher
from .serealization import TeacherSerializer

from .rest.rest import make_rest


professores_get_index, professores_index_by_pk = make_rest(Teacher, TeacherSerializer)
