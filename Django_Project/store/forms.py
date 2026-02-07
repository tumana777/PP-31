from django import forms
from store.models import Product

# class AddProductForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product title', 'class': 'form-control'}))
#     quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Product quantity', 'class': 'form-control'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Product price'}))
#     # description = forms.CharField(required=False, widget=)

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = ['title', 'quantity', 'price', 'description', 'category']
        exclude = ['is_available']
        widgets = {}