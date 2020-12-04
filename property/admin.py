from django.contrib import admin

from .models import Flat




class AdminFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['owner', 'address', 'owners_phonenumber',
                   'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']

admin.site.register(Flat, AdminFlat)