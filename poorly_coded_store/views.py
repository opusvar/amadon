from django.shortcuts import render, redirect
from .models import Order, Product, User_Order

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_checkout(request):
    request.session["quantity"] = int(request.POST["quantity"])
    request.session["price"] = float(request.POST["price"])
    request.session["total_charge"] = float(request.session["quantity"] * request.session["price"])
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=request.session["quantity"], total_price=request.session["total_charge"])
    return redirect("/checkout/") 


def checkout(request):
    quantity_from_form = request.session["quantity"]
    price_from_form = request.session["total_charge"]
    total_charge = request.session["total_charge"]
    total_spent = 0
    for Order.total_price in Order.objects.all():
        print(Order.total_price)
    context = {
        "quantity_from_form" : quantity_from_form,
        "price_from_form" : price_from_form,
        "total_charge": total_charge,
        "total_spent" : total_spent
    }
    return render(request, "store/checkout.html", context) 