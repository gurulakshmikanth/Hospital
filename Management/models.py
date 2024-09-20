from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField()
    specialization=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Patient(models.Model):
    lis=[('Male','male'),('Female','female')]
    pname=models.CharField(max_length=100)
    gender=models.CharField(max_length=6,choices=lis)
    pmobile=models.IntegerField()
    address=models.CharField(max_length=150)
    fees=models.IntegerField(default=0)
    paid=models.IntegerField(default=0)
    balance=models.IntegerField(default=0)
    pay=models.IntegerField(default=0)
    discharge=models.BooleanField(default=False)

    def __str__(self):
        return self.pname

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

    def __str__(self):
        return self.doctor.name+'--'+ self.patient.pname
