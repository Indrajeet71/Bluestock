from django.contrib import admin
from .models import IPOCompany

@admin.register(IPOCompany)
class IPOCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'issue_price', 'lot_size', 'open_date', 'close_date']
