from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.CASCADE,
        related_name="orders"
    )
    channel = models.ForeignKey(
        'channel.Channel',
        on_delete=models.CASCADE,
        related_name="orders"
    )
    status = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:    
        db_table = "orders"

class OrderItem(models.Model):
    order = models.ForeignKey(
        'order.Order',
        on_delete=models.CASCADE,
        related_name="orderItems"
    )
    item = models.ForeignKey(
        'inventory.Item',
        on_delete=models.CASCADE,
        related_name="orderItems"
    )
    qty = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:    
        db_table = "order_items"        
