from django.db import models
from django.db.models.base import ModelState


class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    
    

    def __str__(self):
        return f'{self.name}'
    


class Resource(models.Model):
    name = models.CharField(max_length=200)
    date_acquisition = models.DateField(auto_now=True)
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
    reserve_date = models.DateField(auto_now=True, null=True)


    def __str__(self):
        return f'agendamento de recurso'