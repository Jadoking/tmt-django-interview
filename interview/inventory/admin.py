from django.contrib import admin
from interview.inventory.models import Inventory, InventoryType, InventoryLanguage, InventoryTag


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('type', 'language')
    filter_horizontal = ('tags',)


@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(InventoryLanguage)
class InventoryLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(InventoryTag)
class InventoryTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('is_active',)
