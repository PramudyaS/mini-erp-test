from django.shortcuts import get_object_or_404, redirect, render

from customer.forms import CustomerForm
from .models import Customer

# Create your views here.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/list.html", {"customers": customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, "customer/detail.html", {"customer": customer})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()

    return render(request, "customer/create.html",{"form": form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, "customer/edit.html", {"customer":customer})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk = pk)
    
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid:
        form.save()
        return redirect("customer_list")
    else:
        form = CustomerForm(instance=customer)

    return render(request, "customer/edit.html", {"form": form, "customer": customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_list")

    return redirect("customer_list")
