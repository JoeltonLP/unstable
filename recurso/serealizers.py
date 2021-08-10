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

        result = super().encode(inst)

        result.update(
            name=inst.name,
            patrimony_number=inst.patrimony_number,   
        )

        return result

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
            resource=ResourceSerializer.encode(inst.resource),  
        )

        return result

