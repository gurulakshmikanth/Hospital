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
    pname=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    pmobile=models.IntegerField()
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.pname

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

    def __str__(self):
        return self.doctor.name+'--'+ self.patient.pname
