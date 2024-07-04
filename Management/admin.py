from django.contrib import admin

# Register your models here.
from Management.models import *

admin.site.register(Doctor)

admin.site.register(Patient)
admin.site.register(Appointment)