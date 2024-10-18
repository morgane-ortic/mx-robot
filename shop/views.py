from django.shortcuts import render, HttpResponseRedirect

from shop.models import Product, Customer, Order

# Create your views here.
def list_products(request):
    all_products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': all_products})

def detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
        return render(request, 'shop/detail.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseRedirect('/')