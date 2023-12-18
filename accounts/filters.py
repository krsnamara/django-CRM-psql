import django_filters
from django import forms
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte" , label="Start Date", widget=forms.DateInput(attrs={ 'style': 'max-width: 150px;'}), )
    end_date = DateFilter(field_name="date_created", lookup_expr="lte", label="End Date", widget=forms.DateInput(attrs={ 'style': 'max-width: 150px;'}),)
    note = CharFilter(field_name="note", lookup_expr="icontains", widget=forms.TextInput(attrs={ 'style': 'max-width: 100px;'}),)

    
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ["customer", "date_created"]