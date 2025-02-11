from django import forms

class MagazineForm(forms.Form):
    background_color = forms.CharField(max_length=7, initial="#FFFFFF")
    font_color = forms.CharField(max_length=7, initial="#000000")
    font_size = forms.IntegerField(initial=30, min_value=10, max_value=100)
    font_family = forms.CharField(max_length=100, initial="Arial")
    text_message = forms.CharField(widget=forms.Textarea, required=False)
    cover_image = forms.ImageField()
