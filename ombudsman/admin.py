from django.contrib import admin
from ombudsman.models import *

class ApiKeyGrantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'updated')
    date_hierarchy = 'created'

admin.site.register(ApiKeyGrant, ApiKeyGrantAdmin)
