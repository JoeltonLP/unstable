import json
from django.http import HttpResponse, response
from .models import LoanLogs, Resource, ResourceDataShow, Teacher, LoanResource

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

    @classmethod
    def logs(cls, inst):
        
        dic = {
            'teacher_id': inst.pk,
            'type': 1
        }

        return LoanLogsSerializer.decode(dic)


class ResourceSerializer(BaseSerializer):

    _model = Resource


    @classmethod
    def encode(cls, inst):

        result = super().encode(inst)

        result.update(
            name=inst.get_resource_type_display()   
        )

        return result

    @classmethod
    def logs(cls, inst):
        
        dic = {
            'resource_id': inst.pk,
              'type': 2
        }

        return LoanLogsSerializer.decode(dic)
        

class ResourceDataShowSerializer(BaseSerializer):

    _model = ResourceDataShow

    @classmethod
    def encode(cls, inst):

        result = super().encode(inst)

        result.update(
            name=inst.get_resource_type_display(),
            patrimony_number=inst.patrimony_number,
            full=inst.full_data_show    
        )

        return result

    # @classmethod
    # def logs(cls, inst):
        
    #     dic = {
    #         'resource_id': inst.pk,
    #           'type': 2
    #     }

    #     return LoanLogsSerializer.decode(dic)

class LoanResourceSerealizer(BaseSerializer):

    _model = LoanResource

    @classmethod
    def encode(cls, inst):
        result = super().encode(inst)

        result.update(
            description='Recurso agendado',
            reserve_date=str(inst.reserve_date),
            day_shift=inst.get_day_shift_display(),
            class_room=inst.class_room,
            time=inst.get_time_display(),
            loan_note=inst.loan_note,  
            teacher=TeacherSerializer.encode(inst.teacher),
            resource=ResourceDataShowSerializer.encode(inst.resource),  
        )

        return result
   
    @classmethod
    def logs(cls, inst):
        
        dic = {
            'loan_resource_id': inst.pk,
            'type': 3
        }

        return LoanLogsSerializer.decode(dic)


class LoanLogsSerializer(BaseSerializer):

    _model = LoanLogs

    @classmethod
    def encode(cls, inst):

        
        if inst.type == 1:

            result = {
                'pk_loger': inst.pk
            }

            result.update(
                teacher=TeacherSerializer.encode(inst.teacher)
            )
            return result
        elif inst.type == 2:

            result = {
                'pk_loger': inst.pk
            }

            result.update(
                resource=ResourceSerializer.encode(inst.resource)
            )
            return result
        elif inst.type == 3:

            result = {
                'pk_loger': inst.pk
            }

            result.update(
               loan_resource=LoanResourceSerealizer.encode(inst.loan_resource)
            )

            return result



