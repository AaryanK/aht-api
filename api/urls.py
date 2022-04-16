from django.urls import path

from .views import *
urlpatterns = [
    # path('domestic_search/',domestic_search,name="Domestic Search"),
    # path('bds/',book_domestic_ticket,name="Domestic Book"),
    path('customers/', customers),
    # path('customers/<int:customerid>/bills',get_all_bills_from_customer),
    # path('customers/<int:customerid>/bills/<int:billid>',get_bill_from_customer),
    # path('customers/<int:customerid>/ticket',get_all_tickets_from_customer),
    # path('customers/<int:customerid>/ticket/<int:ticketid>',get_ticket_from_customer),
    path('bookings/',bookings),
    path('test/',insert),
    path('tickets/',tickets)
    ]