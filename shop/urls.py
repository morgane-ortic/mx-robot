from django.urls import path
from shop.views import home, login, log_out, register, detail, list_categories, sort_category, add_to_cart

app_name = 'shop'
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('log_out/', log_out, name='log_out'),
    path('register/', register, name='register'),
    path('product/<int:pk>/', detail, name='detail'),
    path('categories/', list_categories, name='categories'),
    path('category/<str:category>/', sort_category, name='category'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),  # URL for adding product to cart
    # path('view_cart/', view_cart, name='view_cart'),
]