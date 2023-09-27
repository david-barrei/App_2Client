from django.contrib import admin
from .models import *


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nom', 'ap', 'am','lenguaje','SO','area']
    search_fields = ['nom','ap','am']
    list_filter = ['lenguaje','area']
    list_per_page = 5

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Lenguaje)
admin.site.register(SO)
