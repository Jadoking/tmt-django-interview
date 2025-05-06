from django.contrib import admin
from interview.order.models import Order, OrderTag


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventory', 'start_date', 'embargo_date', 'is_active')
    search_fields = ('inventory__name',)
    list_filter = ('start_date', 'embargo_date', 'is_active')
    filter_horizontal = ('tags',)


@admin.register(OrderTag)
class OrderTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active',)
