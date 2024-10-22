from django.shortcuts import render, redirect, HttpResponseRedirect

from shop.models import Product, Customer, Order, Cart


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

def add_to_cart(request, pk):
    product = Product.objects.get(id=pk)

    if 'temp_customer_id' not in request.session:
        temp_customer = Customer.objects.create(first_name='Temp', last_name='Customer')
        request.session['temp_customer_id'] = temp_customer.id
    else:
        temp_customer = Customer.objects.get(id=request.session['temp_customer_id'])
    customer = temp_customer

    # Add the product to the cart
    cart_item, created = Cart.objects.get_or_create(customer=customer, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('shop:list_products')