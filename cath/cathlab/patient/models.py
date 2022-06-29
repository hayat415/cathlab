from django.db import models
import datetime
from tinymce.models import HTMLField

class Procedure(models.Model):
    procedure_type=models.CharField(max_length=10)
    Date=models.DateField()
    discharge_date=models.DateField()
    Cost=models.IntegerField()

    def __str__(self):
        return self.procedure_type

        
class Operator(models.Model):
    name=models.CharField(max_length=15)
    designation=models.CharField(max_length=20)
    def __str__(self):
        return self.name
   

class PCI(models.Model):
    PCI_title=models.CharField(max_length=100)
    PCI_desc=HTMLField()

class Angio(models.Model):
    first_artery=HTMLField()
    second_artery=HTMLField()   
    third_artery=HTMLField()
    fourth_atery=HTMLField()

class Patient(models.Model):
    name=models. CharField(max_length=20)
    age=models.IntegerField()
    sex=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    procedure=models.ForeignKey(Procedure, blank=True, null=True, on_delete=models.CASCADE)
    cnic=models.IntegerField()
    indication=models.CharField(max_length=40)
    visit_number=models.IntegerField()
    operator=models.ForeignKey(Operator, blank=True, null=True, on_delete=models.CASCADE)
    def __str__ (self):
        return self.name 