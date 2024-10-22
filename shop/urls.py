from django.urls import path
from shop.views import add_to_cart, detail, list_categories, sort_category, list_products

app_name = 'shop'
urlpatterns = [
    path('', list_products, name='list_products'),
    path('product/<int:pk>/', detail, name='detail'),
    path('categories/', list_categories, name='categories'),
    path('category/<str:category>/', sort_category, name='category'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),  # URL for adding product to cart
    path()
]