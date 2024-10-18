from django.shortcuts import render, redirect, HttpResponseRedirect

from shop.models import Product, Customer, Order


def list_products(request):
    all_products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': all_products})


def detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
        return render(request, 'shop/detail.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseRedirect('/')
    
def list_categories(request):
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'shop/categories.html', {'categories': categories})

def sort_category(request, category):
    category_products = Product.objects.filter(category=category)
    if not category_products.exists():
        return redirect('/')
    return render(request, 'shop/index.html', {'products': category_products})