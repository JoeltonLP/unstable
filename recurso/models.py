from django.db import models
from django.db.models.base import ModelState
from django.db.models.enums import Choices


class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    

    def __str__(self):
        return f'{self.name}'
    

class Resource(models.Model):
    name = models.CharField(max_length=200)
    patrimony_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class ResourceDataShow(Resource):
    pass


class ResourceQuadra(Resource):
    pass


class ResourceAuditorio(Resource):
    pass


class ResourceCaixaSom(Resource):
    pass


class LoanResource(models.Model):

    teacher = models.OneToOneField(Teacher, on_delete=models.PROTECT)
    resource = models.OneToOneField(Resource, on_delete=models.PROTECT)
    reserve_date = models.DateField(auto_now=True)
    day_shift = models.SmallIntegerField(choices=(
        (1, 'Noite'),
        (2, 'Manha')
    ))
    class_room = models.CharField(max_length=4, null=True)
    time = models.SmallIntegerField(choices=(
        (1, 'Primeiro Horario'),
        (2, 'Segundo Horario')
    ), null=True)
    loan_note = models.CharField(max_length=200, null=True)

    
    class Meta:

        verbose_name_plural = 'Agendamentos'
        verbose_name = 'Agendamentos'

    
    def __str__(self):
        return f'{self.teacher}'


class LoanLogs(models.Model):
    
    loan_resource = models.ForeignKey(LoanResource, related_name="logs", 
        on_delete=models.PROTECT, null=True)
    resource = models.ForeignKey(Resource, related_name='loanlogs', 
        on_delete=models.PROTECT, null=True)
    teacher = models.ForeignKey(Teacher, related_name='teachers', 
        on_delete=models.PROTECT, null=True)
    type = models.SmallIntegerField(choices=(
        (1, 'teacher'),
        (2, 'resource'),
        (3, 'loan_resource')
    ))

    def __str__(self):
        
        return f'{self.teacher}'

   

    

