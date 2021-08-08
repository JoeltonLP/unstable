import json

from django.http import HttpResponse



def make_rest(serealizer):

    model = serealizer._model

    def get_all(request):
    
        query = model.objects.all()

        if query.exists():
            
            inst_serialized = [serealizer.encode(items) for items in query]
            
        
            response = HttpResponse(
                status=200,
                content_type='Application/josn',
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


    def get_by_pk(request, pk, model, serealizer):


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


    def create_index(request, model, serealizer):

    

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


    def put_by_pk(request, pk, model, serealizer):
        
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


    def delete_by_pk(request, pk, model, serealizer):

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

        if request.method == 'GET':
            response = get_all(request)
        elif request.method == 'POST':
            response = create_index(request)

        return response
    

    def _index_by_pk(request, pk):
        
        response = None

        if request.method == 'GET':
            response = get_by_pk(request, pk)

        elif request.method == 'DELETE':
            response = delete_by_pk(request, pk)

        elif request.method == 'PUT':
            response = put_by_pk(request, pk)

        return response 
    
    
    return _index, _index_by_pk