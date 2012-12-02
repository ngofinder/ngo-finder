from django.contrib import admin
from directory.models import *

#class OrganizationAdmin(models.Model):
#    pass

#class

admin.site.register(Organization)
admin.site.register(Sector)
admin.site.register(Location)
admin.site.register(Operation)
admin.site.register(Contact)
admin.site.register(Comment)
