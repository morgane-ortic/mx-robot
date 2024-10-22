from django.urls import path
from shop.views import detail, list_categories, sort_category, list_products

app_name = 'shop'
urlpatterns = [
    path('', list_products, name='list_products'),
    path('product/<int:pk>/', detail, name='detail'),
    path('categories/', list_categories, name='categories'),
    path('category/<str:category>/', sort_category, name='category'),
]