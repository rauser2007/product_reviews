from django.shortcuts import render, get_object_or_404
from .models import Product, Review

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'reviews/product_list.html', {'products': products})

def product_detail(reauest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(reauest, 'reviews/product_detail.html', {'product': product})