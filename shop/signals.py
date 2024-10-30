from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()

@receiver(post_delete, sender=Customer)
def delete_associated_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()