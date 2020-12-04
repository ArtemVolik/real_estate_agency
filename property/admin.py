from django.contrib import admin
from .models import Flat, Complaint, Owner


class AdminFlat(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['get_owner_name', 'address', 'get_owner_phonenumber',
                    'get_owner_pure_phone', 'price', 'new_building',
                    'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']


class AdminComplaint(admin.ModelAdmin):
    raw_id_fields = ('complaint_author', 'complaint_flat')


class AdminOwner(admin.ModelAdmin):
    raw_id_fields = ('flat_in_property',)


admin.site.register(Complaint, AdminComplaint)
admin.site.register(Flat, AdminFlat)
admin.site.register(Owner, AdminOwner)
