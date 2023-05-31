from django.contrib import admin
from . models import WorkImage, Enquiry, Client, ServiceImage, OtherImage

# Register your models here.

@admin.register(WorkImage)
class WorkImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'source']

@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'source']

@admin.register(OtherImage)
class OtherImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'source']

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'subject', 'message']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'work_desc']