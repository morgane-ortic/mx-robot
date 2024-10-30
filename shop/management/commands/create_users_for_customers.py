from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from shop.models import Customer

class Command(BaseCommand):
    help = 'Create User instances for Customers without linked Users'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.filter(user__isnull=True)
        for customer in customers:
            username = f"{customer.first_name.lower()}.{customer.last_name.lower()}"
            email = f"{username}@example.com"
            user = User.objects.create_user(username=username, email=email, password='defaultpassword')
            customer.user = user
            customer.save()
            self.stdout.write(self.style.SUCCESS(f'Created User for Customer: {customer}'))