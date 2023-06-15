from django import forms
from ..models.cart import Cart

class CartForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1, label='Quantity', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    class Meta:
        model = Cart
        fields = ['quantity', 'update']

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['max'] = self.product.stock
        self.fields['quantity'].widget.attrs['min'] = 1

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity > self.product.stock:
            raise forms.ValidationError("Only {} available".format(self.product.stock))
        return quantity

