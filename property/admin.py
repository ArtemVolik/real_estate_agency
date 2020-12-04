from django.contrib import admin
from .models import Flat, Complaint




class AdminFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['owner', 'address', 'owners_phonenumber',
                   'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('complaint_author', 'complaint_flat')


admin.site.register(Complaint, AdminComplaint)
admin.site.register(Flat, AdminFlat)
