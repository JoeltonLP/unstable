from django.http import HttpResponse, response
from .models import Resource, Teacher


class BaseSerializer:

    _model = None

    @classmethod
    def serealizer(cls, inst):
        
        data = {
            "pk": inst.pk,
            "name": inst.name,
            "email": inst.email,
            "phone": inst.phone
        }

        return data

    @classmethod
    def deserealizer(cls, data):

        inst = cls._model(**data )

        return inst


class TeacherSerializer(BaseSerializer):

    _model = Teacher


class ResourceSerializer(BaseSerializer):

    _model = Resource


    @classmethod
    def serealizer(cls, inst):
        
        response = {
            'pk': inst.pk,
            'name': inst.name
        }
        return response

