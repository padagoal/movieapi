from django.contrib import admin
from .models import Person,Movies
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

class PersonAdmin(admin.ModelAdmin):
    list_display =('lastname','firstname','aliases','is_actor','is_director','is_producer')


admin.site.register(Person,PersonAdmin)
admin.site.register(Movies)