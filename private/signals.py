from django.db.models.signals import post_save
from .models import Booking,Customer,CustomerID, Ticket,Bill
from django.dispatch import receiver

from .models import Customer



import string
import random

def create_code():
    letters = string.ascii_letters+string.digits
    letters = list(letters)
    random.shuffle(letters)
    return "".join(letters[:6])

@receiver(post_save, sender=Customer)
def learner_profile(sender, instance, created, **kwargs):
    if created:

        code = create_code()
        if Customer.objects.filter(cid__cid=code).count() == 0:
            instance.cid = CustomerID.objects.create(cid=create_code())
            instance.save()

@receiver(post_save,sender=Ticket)
def bill_create(sender, instance, created, **kwargs):
    if created:
        if Bill.objects.all().count() !=0:
            bill_number = Bill.objects.all().last().bill_number +1
        else:
            bill_number = 1
        a = Bill()
        a.bill_number = bill_number
        a.ticket = instance
        a.payment_received = True
        a.save()
        
