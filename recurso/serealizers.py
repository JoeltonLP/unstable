from django.http import HttpResponse, response
from .models import Resource, Teacher, LoanResource

from helpers.serializer import BaseSerializer


class TeacherSerializer(BaseSerializer):

    _model = Teacher

    @classmethod
    def encode(cls, inst):
        result = super().encode(inst)

        result.update(
            name=inst.name,
            email=inst.email,
            phone=inst.phone  
        )

        return result


class ResourceSerializer(BaseSerializer):

    _model = Resource


    @classmethod
    def encode(cls, inst):
        
        response = {
            'name': inst.name
        }
        return response

class LoanResourceSerealizer(BaseSerializer):

    _model = LoanResource

    @classmethod
    def encode(cls, inst):
        result = super().encode(inst)

        result.update(
            description='Recurso agendado', 
            teacher=TeacherSerializer.encode(inst.teacher),
            resource=ResourceSerializer.encode(inst.resource)
        )

        return result

