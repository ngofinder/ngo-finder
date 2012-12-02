from django.contrib import admin
from directory.models import *

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name','url',)

class SectorAdmin(admin.ModelAdmin):
    pass

class Geo_scopeAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Sector,SectorAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Geo_scope,Geo_scopeAdmin)
admin.site.register(Operation)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment)
