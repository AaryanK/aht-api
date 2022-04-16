from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Ticket)
admin.site.register(Bill)
admin.site.register(Booking)
admin.site.register(CustomerID)
admin.site.register(Commission)
admin.site.register(Airline)
