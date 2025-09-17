from django.contrib import admin

from inventory.models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','current_qty','created_at','updated_at')