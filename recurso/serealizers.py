from django.http import HttpResponse, response
from .models import Resource, Teacher, LoanResource

from helpers.serializer import BaseSerializer


class TeacherSerializer(BaseSerializer):

    _model = Teacher


class ResourceSerializer(BaseSerializer):

    _model = Resource


    @classmethod
    def encode(cls, inst):
        
        response = {
            'pk': inst.pk,
            'name': inst.name
        }
        return response

class LoanResourceSerealizer(BaseSerializer):

    _model = LoanResource

    @classmethod
    def encode(cls, inst):
        
        response = {
            'pk': inst.pk,
            'teacher_id': inst.teacher_id,
            'name_techer': inst.teacher.name,
            'resource_id': inst.resource_id,
            'name_resource': inst.resource.name,
            
        }
        return response

