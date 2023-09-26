from .models import Product
from django.forms import ModelForm, TextInput, NumberInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'descriptions', 'price']

        widgets = {
            "title": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Название продукта'
            }),
            "descriptions": TextInput(attrs={
                "class": 'form-control',
                'placeholder': 'Описание продукта'
            }),
            "price": NumberInput(attrs={
                "class": 'form-control',
                'placeholder': 'Цена продукта'
            }),
        }
