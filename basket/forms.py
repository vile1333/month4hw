from django import forms
from basket.models import Basket

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = '__all__'
