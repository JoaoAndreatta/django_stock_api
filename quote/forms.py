from django import forms
from .models import Stock_db

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock_db
        fields = ["ticker"]