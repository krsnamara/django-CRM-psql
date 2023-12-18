from django.forms import ModelForm
from .models import Order
from .models import Product
from .models import Customer

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category')  # You can adjust this based on your actual model fields

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"  # You can adjust this based on your actual model fields


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

