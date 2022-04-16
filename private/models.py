from django.db import models
from django.db.models import manager
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


# from api.serializers import CustomerSerializers
# Create your models here.

class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomerID(models.Model):
    cid = models.CharField(max_length=150,null=True)
    
    def __str__(self):
        return self.cid


class Customer(models.Model):
    cid = models.OneToOneField(CustomerID,on_delete=models.CASCADE,null=True)
    nationality_choices = ("Nepali","Nepali"),("Indian","Indian"),("Foreign","Foreign")
    name = models.CharField(max_length=500,null=True,unique=True)
    email = models.EmailField(unique=False,null=True,blank=True)
    phone_number = PhoneNumberField(unique=False,null=True,blank=True)
    type = models.CharField(choices=(("Adult","Adult"),("Child","Child")),null=True,max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    nationality = models.CharField(choices =nationality_choices,max_length=100,null=True)

    def __str__(self):
        return str(self.name)




class Ticket(models.Model):
    from_sector = models.CharField(max_length=50)
    to_sector = models.CharField(max_length=50)
    passenger_name = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=10)
    pnr = models.CharField(max_length=10,null=True)
    airlines = models.ForeignKey(Airline,on_delete=models.SET_NULL,null=True)
    flight_date = models.DateField(null=True)
    flight_time = models.TimeField(null=True)
    fare = MoneyField(max_digits=14,default_currency='NPR')
    ticket_class = models.CharField(max_length=5,blank=True,null=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.airlines.name} {self.pnr} {self.ticket_number} "



class Bill(models.Model):
    bill_number = models.IntegerField()
    ticket = models.OneToOneField(Ticket,on_delete=models.CASCADE)
    payment_received = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.ticket.passenger_name.name}'s {self.ticket.from_sector} TO {self.ticket.to_sector}"







# class Passenger(models.Model):
#     nationality_choices = ("Nepali","Nepali"),("Indian","Indian"),("Foreign","Foreign")
#     full_name = models.CharField(max_length=100)
#     passenger_type = models.Choices("Child","Adult")
#     nationality = models.CharField(choices = nationality_choices,max_length=100)
#     phone_number = PhoneNumberField(unique=True)


class Booking(models.Model):
    airline = models.ForeignKey(Airline,on_delete=models.SET_NULL,null=True)
    pnr = models.CharField(max_length=10,null=True,unique=True)
    flight_number = models.CharField(max_length=100,null=True)
    sector = models.CharField(max_length=10,null=True)
    flight_date = models.DateField(null=True)
    flight_time = models.TimeField(null=True)
    passengers = models.ManyToManyField(Customer,blank=True)
    expires_on = models.DateTimeField(null=True) 
    class_name = models.CharField(null=True,max_length=100)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticketed = models.BooleanField(default=False)
    nop = models.IntegerField(null=True,blank=True)
    unit_price = models.IntegerField(null=True)

    def __str__(self):
        return self.pnr

    def natural_key(self):
        return (self.name)


class Commission(models.Model):
    ticket = models.OneToOneField(Ticket,on_delete=models.CASCADE)
    commission = MoneyField(max_digits=14,default_currency='NPR')

    def __str__(self):
        return str(self.commission)