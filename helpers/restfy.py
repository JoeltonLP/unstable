import json

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render


def make_rest(serializer, allow_get=True, allow_by_id=True, allow_post=True, 
            allow_update=True, allow_delete=True):

    model = serializer._model

    def get_all(request):
    
        query = model.objects.all()

        if query.exists():
            
            inst_serialized = [serializer.encode(items) for items in query]
            
        
            response = HttpResponse(
                status=200,
                content_type='application/json',
                content=json.dumps(inst_serialized)   
            )
        else:
            response = HttpResponse(
                status=404,
                content_type='Application/json',
                content=json.dumps({
                    'Menssage': 'Nenhum item na base de dados'
                })
            )

        
        return response


    def get_by_id(request, id):


        try:

            inst = model.objects.get(id=id)
            inst_serealized = serializer.encode(inst)


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
                    'Message': f'O item com a id {id} nao existe'
                })
            )

        return response

    def create_index(request):

        
        
        request_data = json.loads(request.body)
        
        try:
           
            inst = serializer.decode(request_data)
            inst.save()

            # inst_logs = serializer.logs(inst)
            # inst_logs.save()
            
            inst_serealized = serializer.encode(inst)

            response = HttpResponse(
                status=201,
                content_type='Application/json',
                content=json.dumps([inst_serealized])
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


    def put_by_id(request, id):
        
        request_data = json.loads(request.body)

        try:

            inst = model.objects.get(id=id)

            for key, value in request_data.items():

                setattr(inst, key, value)

            inst.save()  

            inst_serialized = serializer.encode(inst)

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
                    'Message': str(e)
                })
            )

        return response


    def delete_by_id(request, id):

        try:
           
            inst = model.objects.get(id=id)
            inst.delete()
            
           

            response = HttpResponse(
                status=200,
                content_type='Application/josn',
                content=json.dumps({
                    'Message': f'item com a id {id} foi deletado com sucesso'
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


    def _index(request):

        if allow_get and request.method == 'GET':
            response = get_all(request)
        elif allow_post and request.method == 'POST':
            response = create_index(request)
        else:
            response = HttpResponse(status=405)

        return response
    

    def _index_by_id(request, id):
        
        response = None

        if allow_by_id and request.method == 'GET':
            response = get_by_id(request, id)

        elif allow_delete and request.method == 'DELETE':
            response = delete_by_id(request, id)

        elif allow_update and request.method == 'PUT':
            response = put_by_id(request, id)
        else:
            response = HttpResponseNotAllowed(permitted_methods=['GET'])

        return response 
     
    return _index, _index_by_id