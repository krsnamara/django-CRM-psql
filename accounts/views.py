from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .forms import ProductForm
from .forms import CustomerForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {"orders": orders, "customers": customers, "total_orders": total_orders, "delivered": delivered, "pending": pending}

    return render(request, "accounts/dashboard.html", context)
    
def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})

def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()

    return render(request, "accounts/create_product.html", {"form": form})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {"customer": customer, "orders": orders, "total_orders": total_orders, "myFilter": myFilter}
    return render(request, "accounts/customer.html", context)

def createCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CustomerForm()

    return render(request, "accounts/create_customer.html", {"form": form})    

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer", pk_test=customer.id)
    else:
        form = CustomerForm(instance=customer)

    return render(request, "accounts/update_customer.html", {"form": form, "customer": customer})

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status", "note"), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={"customer": customer})
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")

    context = { "formset": formset}
    return render(request, "accounts/order_form.html", context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        # print("Printing POST:", request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("customer", pk_test=order.customer.id)

    context = { "form": form,}
    return render(request, "accounts/update_order.html", context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context = { "item": order,}
    return render(request, "accounts/delete.html", context)
