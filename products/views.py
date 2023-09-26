from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def product(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {"products": products})


def createproduct(request):
    error = ''
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            error = "Ошибка"
    form = ProductForm()

    data = {
        "form": form,
        "error": error
    }
    return render(request, 'products/create.html', data)
