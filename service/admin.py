from django.contrib import admin
from service.models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_title', 'service_description')
    
admin.site.register(Service, ServiceAdmin)