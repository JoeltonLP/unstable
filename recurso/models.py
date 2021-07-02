from django.db import models

class Teacher(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100, unique=True)
    


    def __str__(self):
        return f'{self.name}/{self.email}'
