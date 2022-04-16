from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer,SlugRelatedField
from .models import Bill, Booking, Customer, Ticket,CustomerID



class CustomerIdSerializers(ModelSerializer):
    class Meta:
        model = CustomerID
        fields = '__all__'

class CustomerSerializers(ModelSerializer):
    cid = SlugRelatedField(
        read_only=True,
        slug_field='cid'
    )
    class Meta:
        model = Customer
        fields = '__all__'
        
class BillSerializers(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class TicketSerializers(ModelSerializer):
    class Meta:
        model = Ticket
        fields='__all__'

class BookingSerializers(ModelSerializer):
    passengers = CustomerSerializers(read_only=True,many=True)
    class Meta:
        model = Booking
        fields = (
        'airline',
        'pnr',
        'flight_number',
        'sector',
        'flight_date',
        'flight_time',
        'passengers',
        'expires_on',
        'class_name',
        'booked_on',
        'ticketed',
        'nop',
        'unit_price')
        