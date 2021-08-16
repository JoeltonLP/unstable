import json
from recurso.models import ResourceDataShow
from django.http import response
from django.http.response import HttpResponse
from .serealizers import (
    TeacherSerializer, 
    ResourceSerializer, 
    LoanResourceSerealizer,
    LoanLogsSerializer,
    ResourceDataShowSerializer
)

from helpers import restfy


professor_index, professor_by_id = restfy.make_rest(TeacherSerializer)
recurso_index, recurso_by_id = restfy.make_rest(ResourceDataShowSerializer)
recurso_data_show_index, recurso_data_show_by_id = restfy.make_rest(ResourceDataShowSerializer)
agendamento_index, agendamento_by_id = restfy.make_rest(LoanResourceSerealizer)
get_log_index , get_log_by_id = restfy.make_rest(
    LoanLogsSerializer,
    allow_delete=False,
    allow_post=False,
    allow_update=False    
)




from .serealizers import LoanLogs

# def _list(request):
    
#     try:

#         query = LoanLogs.objects.all()
        
#         inst_serialized = [LoanLogsSerializer.encode(log) for log in query]
            
#         return HttpResponse(
#             status=200,
#             content_type='Application/josn',
#             content=json.dumps(inst_serialized)

#         )
    
#     except Exception as e:
#         print(e)

#         return HttpResponse(
#             status=400, 
#             content=json.dumps({
#                 'message': str(e)
#             })
#         )



def register_log_index(request):


    if request.method == 'GET':

        return HttpResponse(status=501)

    elif request.method == 'POST':
    
        response = HttpResponse(status=405)

    return response


def register_log_by_id(request, pk):
   

    if request.method == 'GET':
        response = HttpResponse(status=501)

    elif request.method == 'DELETE':
        response = HttpResponse(status=405)

    elif request.method == 'PUT':
        response = HttpResponse(status=405)

    return response 
 
    
    