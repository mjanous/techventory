from techventory.models import *
from django.contrib import admin

class ApplicationVersionInline(admin.TabularInline):
    model = ApplicationVersion
    extra = 1

class ApplicationAdmin(admin.ModelAdmin):
    inlines = [ApplicationVersionInline]
    
admin.site.register(Server)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationVersion)