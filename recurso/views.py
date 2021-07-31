import json

from django.http import HttpResponse, response
from .serealization import TeacherSerializer

from .models import Teacher



def get_all(request):
    
    query = Teacher.objects.all()

    if query.exists():

        inst_serialized = [TeacherSerializer.serealizer(teachers) for teachers in query]

     
        response = HttpResponse(
            status=200,
            content_type='Application/josn',
            content=json.dumps(inst_serialized)   
        )
    else:
        response = HttpResponse(
            status=404
        )

    return response


def get_by_pk(request, pk):


    try:

        inst = Teacher.objects.get(pk=pk)
        inst_serealized = TeacherSerializer.serealizer(inst)


        response = HttpResponse(
            status=200,
            content_type='Application/josn',
            content=json.dumps([
                inst_serealized
            ])
            
        )

    except Exception as e:

        response = HttpResponse(
            status=404,
            content_type='Application/josn',
            content=json.dumps({
                'Message': f'O item com a pk {pk} nao existe'
            })
        )

    return response


def create_index(request):

    request_data = json.loads(request.body)

    try:
        
        inst = TeacherSerializer.deserealizer(request_data)
        inst.save()

        x = TeacherSerializer.serealizer(inst)

        response = HttpResponse(
            status=201,
            content=json.dumps([x])
        )

    except Exception as e:
        
        response = HttpResponse(
            status=400,
            content_type='Apllication/json',
            content=json.dumps({
                'Message': str(e)
            })
        )

    return response


def delete_by_pk(request, pk):

    try:

        inst = Teacher.objects.get(pk=pk)
        inst.delete()
        

        response = HttpResponse(
            status=200,
            content_type='Application/josn',
            content=json.dumps({
                'Message': f'item com a pk {pk} foi deletado com sucesso'
            })
        )

    except Exception as e:

        response = HttpResponse(
            status=404,
            content_type='Application/json',
            content=json.dumps(
                {
                    'Message': str(e)
                }
            )
        )
    
    return response


def put_by_pk(request, pk):
    
    request_data = json.loads(request.body)
    

    try:

        inst = Teacher.objects.get(pk=pk)

        for key, value in request_data.items():

            setattr(inst, key, value)

        inst.save()  

        inst_serialized = TeacherSerializer.serealizer(inst)

        response = HttpResponse(
            status=200,
            content_type='Application/json',
            content=json.dumps([inst_serialized])
        )

    except Exception as e:
        
        response = HttpResponse(
            status=400,
            content_type='Apllication/json',
            content=json.dumps({
                'Message': f'o item com  a pk {pk} nao existe'
            })
        )

    return response
    


def index(request):

    if request.method == 'GET':
        response = get_all(request)
    elif request.method == 'POST':
        response = create_index(request)

    return response


def index_by_pk(request, pk):

    response = None

    if request.method == 'GET':
        response = get_by_pk(request, pk)

    elif request.method == 'DELETE':
        response = delete_by_pk(request, pk)

    elif request.method == 'PUT':
        response = put_by_pk(request, pk)

    return response 