from django.shortcuts import render, redirect, HttpResponseRedirect
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from shop.models import Product, Customer, Order, Cart


def home(request):
    all_products = Product.objects.all()
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = User.objects.get(id=user_id)
        return render(request, 'shop/home.html', {'username': user.username, 'products': all_products})
    else:
        return render(request, 'shop/home.html', {'products': all_products})

def login(request):
    if request.method == 'POST':
        # print(request.POST.get('password'))
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('shop:home')
        else:
            return redirect('shop:login')
    return render(request, 'shop/login.html')

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('shop:home')
    return redirect('shop:home')
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        return redirect('shop:login')
    return render(request, 'shop/register.html')


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
    return render(request, 'shop/home.html', {'products': category_products})

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