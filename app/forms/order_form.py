from django import forms
from django.forms.widgets import SelectDateWidget

from ..models.order import Order #ADDRESS_CHOICES


class OrderForm(forms.ModelForm):
    # address_type = forms.ChoiceField(choices=ADDRESS_CHOICES, widget=forms.RadioSelect())
    shipping_date = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    
    class Meta:
        model = Order
        fields = ['address_type', 'shipping_date']
        widgets = {
            'shipping_date': SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"))
        }
