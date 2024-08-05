from django import forms

from Management.models import *

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'

class PatientrForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

