from django.contrib import admin

from order.models import Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer_id','total_amount','tax_amount','status','channel_id','created_at','updated_at')