from techventory.models import *
from django.contrib import admin

class OperatingSystemVersionInline(admin.TabularInline):
    model = OperatingSystemVersion
    extra = 1
    
class OperatingSystemAdmin(admin.ModelAdmin):
    inlines = [OperatingSystemVersionInline]

class ApplicationVersionInline(admin.TabularInline):
    model = ApplicationVersion
    extra = 1

class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationVersionInline]
    
class ServerAdmin(admin.ModelAdmin):
    list_display = (
        'hostname',
        'domain',
        'dop',
    )
    
admin.site.register(Server, ServerAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
