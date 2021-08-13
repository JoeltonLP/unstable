import json

from django.http import HttpResponse
from django.shortcuts import render


def make_rest(serealizer, allow_get=True, allow_by_pk=True, allow_post=True, 
            allow_update=True, allow_delete=True):

    model = serealizer._model

    def get_all(request):
    
        query = model.objects.all()

        if query.exists():
            
            inst_serialized = [serealizer.encode(items) for items in query]
            
        
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

        data = json.loads(response.content)
        print(data)
        return render(request, 'professor.html', data)


    def get_by_pk(request, pk):


        try:

            inst = model.objects.get(pk=pk)
            inst_serealized = serealizer.encode(inst)


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
            
            inst = serealizer.decode(request_data)
            inst.save()

            
            inst_serealized = serealizer.encode(inst)

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


    def put_by_pk(request, pk):
        
        request_data = json.loads(request.body)

        try:

            inst = model.objects.get(pk=pk)

            for key, value in request_data.items():

                setattr(inst, key, value)

            inst.save()  

            inst_serialized = serealizer.encode(inst)

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


    def delete_by_pk(request, pk):

        try:

            inst = model.objects.get(pk=pk)
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
                        'Message': f'O item com a pk {pk} nao existe'
                    }
                )
            )
        
        return response


    def _index(request):

        if allow_get and request.method == 'GET':
            response = get_all(request)
        elif allow_post and request.method == 'POST':
            response = create_index(request)

        return response
    

    def _index_by_pk(request, pk):
        
        response = None

        if allow_by_pk and request.method == 'GET':
            response = get_by_pk(request, pk)

        elif allow_delete and request.method == 'DELETE':
            response = delete_by_pk(request, pk)

        elif allow_update and request.method == 'PUT':
            response = put_by_pk(request, pk)

        return response 
    
    
    return _index, _index_by_pk