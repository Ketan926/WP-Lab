from django.shortcuts import render, redirect
from .forms import GroceryForm

# Prices of the grocery items
PRICES = {
    "Rice": 50,
    "Flour": 40,
    "Milk": 30,
    "Eggs": 5,
    "Fruits": 100,
}

def grocery_list(request):
    form = GroceryForm()
    
    if 'cart' not in request.session:
        request.session['cart'] = []  # Initialize session cart

    cart = request.session.get('cart', [])  # Retrieve cart

    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            selected_items = form.cleaned_data['items']
            cart = [{"name": item, "price": PRICES[item]} for item in selected_items]
            request.session['cart'] = cart  # Store in session
            return redirect('grocery_list')

    total_price = sum(item["price"] for item in cart)  # Calculate total cost

    return render(request, "grocery_app/grocery.html", {
        "form": form,
        "cart": cart,
        "total_price": total_price,
    })
