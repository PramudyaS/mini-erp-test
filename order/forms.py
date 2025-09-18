from django import forms
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "channel", "status", "total_amount", "tax_amount"]
        widgets = {
            "total_amount": forms.NumberInput(attrs={"class": "form-input"}),
            "tax_amount": forms.NumberInput(attrs={"class": "form-input"}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["item", "qty", "total_amount"]
        widgets = {
            "qty": forms.NumberInput(attrs={"class": "form-input"}),
            "total_amount": forms.NumberInput(attrs={"class": "form-input"}),
        }
