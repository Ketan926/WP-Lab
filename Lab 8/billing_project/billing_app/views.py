from django.shortcuts import render
from .forms import BillingForm

# Price dictionary
PRICES = {'Mobile': 15000, 'Laptop': 50000}

def billing_form(request):
    form = BillingForm()
    return render(request, 'billing_app/billing_form.html', {'form': form})

def process_bill(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            products = form.cleaned_data['items']  # Fixed: Changed 'product' to 'items'
            quantity = form.cleaned_data['quantity']

            total_price = sum(PRICES[p] for p in products) * quantity

            return render(request, 'billing_app/bill_summary.html', {
                'brand': brand,
                'products': products,
                'quantity': quantity,
                'total_price': total_price,
            })
    return render(request, 'billing_app/billing_form.html', {'form': BillingForm()})
