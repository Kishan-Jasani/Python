'''
from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    emp_sal = models.FloatField()
    emp_add = models.CharField(max_length=64)
    
    def __str__(self):
        return self.emp_name
        
        
        
        
table_name = databaseapp_employee


'''