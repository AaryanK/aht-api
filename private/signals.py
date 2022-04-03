from django.db.models.signals import post_save
from .models import Customer,CustomerID
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
