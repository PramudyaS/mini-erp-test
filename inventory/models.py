from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    current_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:    
        db_table = "items"

class StockItem(models.Model):
    item_id = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        related_name="stock_items"
    )
    qty = models.IntegerField()
    status = models.CharField(max_length=5,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "stock_items"

