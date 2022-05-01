from django.contrib import admin
from .models import Patient,Pharmacy,Drug,Drugstock,Doctor, PrescribedDrug, Prescription

# Register your models here.

admin.site.register(Patient)
admin.site.register(Pharmacy)
admin.site.register(Drug)
admin.site.register(Drugstock)
admin.site.register(Doctor)
admin.site.register(PrescribedDrug)
admin.site.register(Prescription)