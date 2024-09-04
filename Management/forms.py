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

    def clean_pname(self):
        pname=self.cleaned_data.get('pname')
        if any(char.isdigit() for char in pname):
            raise forms.ValidationError("Name contains string")
        return pname

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

