from msilib.schema import DrLocator
from django.contrib import admin
from .models import Doctor
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("user","grade","description", "created_at", "modified_at")
    

# admin.site.register(Doctor)

