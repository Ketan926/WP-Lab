from django import forms

GROCERY_ITEMS = [
    ('Rice', 'Rice - ₹50/kg'),
    ('Flour', 'Flour - ₹40/kg'),
    ('Milk', 'Milk - ₹30/litre'),
    ('Eggs', 'Eggs - ₹5 each'),
    ('Fruits', 'Fruits - ₹100/kg'),
]

class GroceryForm(forms.Form):
    items = forms.MultipleChoiceField(
        choices=GROCERY_ITEMS,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Grocery Items",
    )
