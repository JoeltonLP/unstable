from django.db import models



class Resource(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return f'{self.name}'



class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.CharField('Email', max_length=100, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    #resource = models.ForeignKey(Resource, related_name='resources', on_delete=models.PROTECT, null=True)
    

    def __str__(self):
        return f'{self.name}'
    


class Scheduling(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='+', on_delete=models.PROTECT)
    resource = models.ForeignKey(Resource, related_name='+', on_delete=models.PROTECT)
    lead_date = models.DateField(auto_now=True)
    lead_return = models.DateField(auto_now=True)
    lead_days =  models.SmallIntegerField()


    def __str__(self):
        pass 
    



