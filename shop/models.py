from django.db import models

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    # CASCADE ensures the reference is deleted if customer is deleted
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # SET_NULL ensure the reference will stay if product is deleted
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField("order date")
    def __str__(self):
        return f"Order by {self.customer} on {self.date}"