from django.shortcuts import get_object_or_404, redirect, render

from inventory.forms import ItemForm
from inventory.models import Item, StockItem
from django.db.models import Sum

# Create your views here.

def view_item(request) :
    items = Item.objects.all()

    return render(request, "inventory/list.html", {
        "items": items
    })

def create_item(request):
    if request.POST:
        form = ItemForm(request.POST)
        print(request.POST)  

        if form.is_valid():
            item = form.save()
            StockItem.objects.create(
                item_id = item,
                qty = item.current_qty,
                status = "in"
            )

            return redirect("view_item")
        else:
            print(form.errors)
    else:
        form = ItemForm()

    return render(request, "inventory/create.html",{"form": form})

def edit_item(request,pk):
    item = get_object_or_404(Item, pk=pk)
    stocks = StockItem.objects.filter(item_id = item.id)

    return render(request, "inventory/edit.html", {
        "item": item,
        "stocks": stocks
    })

def delete_item(request,pk):
    item = get_object_or_404(Item, pk = pk)

    if request.method == "POST":
        item.delete()
        return redirect("view_item")

    return redirect("view_item")

def manage_stock(request,pk):
    item = get_object_or_404(Item, pk = pk)

    if request.POST.get("status", False) == "in":
        StockItem.objects.create(
            item_id = item,
            qty = request.POST.get("qty",0),
            status = "in"
        )
    else:
        StockItem.objects.create(
            item_id = item,
            qty = request.POST.get("qty",0),
            status = "out"
        )    

    sumInStock = StockItem.objects.filter(
        item_id=item.id,
        status="in"
    ).aggregate(total=Sum("qty"))["total"] or 0

    sumOutStock = StockItem.objects.filter(
        item_id=item.id,
        status="out"
    ).aggregate(total=Sum("qty"))["total"] or 0
    
    currentStock = sumInStock - sumOutStock

    item.current_qty = currentStock
    item.save()

    stocks = StockItem.objects.filter(item_id = item.id)
    
    return redirect("edit_item", pk=item.id)
