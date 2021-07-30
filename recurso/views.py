import json

from django.http import HttpResponse
from .serealization import TeacherSerializer

from .models import Teacher



def list_all(request):
    
    query = Teacher.objects.all()

    if query.exists():

        inst = [TeacherSerializer.serealizer(teachers) for teachers in query]

     
        response = HttpResponse(
            status=200,
            content_type='Application/josn',
            content=json.dumps(inst)   
        )
    else:
        response = HttpResponse(
            status=404
        )

    return response


def getOne(request):
    pass


def create(request):

    request_data = json.loads(request.body)

    try:
        
        inst = TeacherSerializer.deserealizer(request_data)
        inst.save()

        response = HttpResponse(
            status=201
        )

    except Exception as e:
        
        response = HttpResponse(
            status=203
        )

    return response



def index(request):

    if request.method == 'GET':
        response = list_all(request)
    elif request.method == 'POST':
        response = create(request)

    return response


def index_by_pk(request, pk):

    if request.method == 'GET':
        response = HttpResponse(
            status=501
        )

    elif request.method == 'POST':
        response = HttpResponse(
            status=501
        )
    return response