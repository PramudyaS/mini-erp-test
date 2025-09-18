from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render

from channel.models import Channel
from customer.models import Customer
from inventory.models import Item
from order.forms import OrderForm, OrderItemForm
from order.models import Order, OrderItem

# Create your views here.
def view(request):
    orders = Order.objects.all()
    return render(request, "order/index.html",{
        "orders": orders
    })

def create(request):
    items = Item.objects.all()
    customers = Customer.objects.all()
    channels = Channel.objects.all()
     
    if request.method == "POST":
        print("POST data:", request.POST)
        data = request.POST.copy()
        data['status'] = 'draft'
        order_form = OrderForm(data)
        errors = []

        if order_form.is_valid():
            print("OrderForm valid")
            order = order_form.save(commit=False)

            item_ids = request.POST.getlist("items[]")
            qtys = request.POST.getlist("qtys[]")
            print("Items:", item_ids, "Qtys:", qtys)

            subtotal = Decimal("0.00")
            order.save()

            if not item_ids:
                errors.append("Please add at least one item.")

            for item_id, qty in zip(item_ids, qtys):
                try:
                    item = Item.objects.get(id=item_id)
                    qty = int(qty) if qty else 0
                except (Item.DoesNotExist, ValueError):
                    continue

                if qty > 0:
                    line_total = item.price * qty
                    subtotal += line_total

                    OrderItem.objects.create(
                        order=order,
                        item=item,
                        qty=qty,
                        total_amount=line_total
                    )

            tax = subtotal * Decimal("0.10")
            total = subtotal + tax

            order.tax_amount = tax
            order.total_amount = total
            order.save()

            return redirect("view")
        else:
            print("OrderForm invalid:", order_form.errors)
            errors.append("Please correct the errors below.")
    else:
        order_form = OrderForm()

    return render(request, "order/create.html", {
        "order_form": order_form,
        "customers": customers,
        "channels": channels,
        "items": items
    })

def edit(request, pk):
    order = get_object_or_404(Order, pk=pk)

    order_form = OrderForm(instance=order)

    items = Item.objects.all()
    customers = Customer.objects.all()
    channels = Channel.objects.all()
   
    statuses = ['draft', 'pending_payment', 'ready_shipment' ,'shipped', 'cancelled' ,'delivered']

    return render(request, "order/edit.html", {
        "order_form": order_form,
        "order": order,
        "customers": customers,
        "channels": channels,
        "items": items,
        "statuses": statuses
    })

def update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = Item.objects.all()
    customers = Customer.objects.all()
    channels = Channel.objects.all()
    errors = []

    print(request.POST)

    if request.method == "POST":
        order_form = OrderForm(request.POST, instance=order)

        if order_form.is_valid():
            print("OrderForm valid")
            order = order_form.save(commit=False)
            order.save()

            item_ids = request.POST.getlist("items[]")
            qtys = request.POST.getlist("qtys[]")
            print("Updating items:", item_ids, "Qtys:", qtys)

            processed_ids = []

            subtotal = Decimal("0.00")

            for item_id, qty in zip(item_ids, qtys):
                try:
                    item = Item.objects.get(id=item_id)
                    qty = int(qty) if qty else 0
                except (Item.DoesNotExist, ValueError):
                    continue

                if qty <= 0:
                    continue

                line_total = item.price * qty
                subtotal += line_total

                order_item, created = OrderItem.objects.update_or_create(
                    order=order,
                    item=item,
                    defaults={"qty": qty, "total_amount": line_total}
                )
                processed_ids.append(order_item.id)

            OrderItem.objects.filter(order=order).exclude(id__in=processed_ids).delete()

            tax = subtotal * Decimal("0.10")
            total = subtotal + tax
            order.tax_amount = tax
            order.total_amount = total
            order.save()

            return redirect("view")
        else:
            print("OrderForm invalid:", order_form.errors)
            errors.append("Please correct the errors below.")
    else:
        order_form = OrderForm(instance=order)

    return render(request, "order/edit.html", {
        "order_form": order_form,
        "order": order,
        "customers": customers,
        "channels": channels,
        "items": items,
        "errors": errors
    })

def cancel(request, pk):
    order = get_object_or_404(Order, pk = pk)

    order.status = "cancelled"
    order.save()
    return redirect("view")
