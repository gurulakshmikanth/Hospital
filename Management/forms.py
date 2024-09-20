from django import forms

from Management.models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
    

class PatientrForm(forms.ModelForm):
    lis=[('Male','male'),('Female','female')]
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=lis)
    class Meta:
        model=Patient
        lis=[('Male','male'),('Female','female')]
        gender=forms.ChoiceField(widget=forms.RadioSelect(choices=lis))
        fields=['pname','gender','pmobile','address','fees','paid','balance','pay','discharge']

    

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

