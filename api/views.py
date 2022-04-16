import json
from os import name
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .Ticket_Sectors.Domestic import main
from private.models import *
from private.serialiazers import *
from rest_framework.parsers import JSONParser
import re


# Create your views here.


    
@api_view(['GET','POST','PUT'])
def customers(request):
    if request.method == "GET":
        if "search" in request.GET:
            searched = request.query_params.get('search')
            matches = []
            for i in Customer.objects.all():
                i = str(i)
                result = re.search(r""+searched, i)
                if result:
                    matches.append(i)
            return Response({"matches":matches})

        if "customerid" in request.GET:
            customer = Customer.objects.filter(cid__cid=request.query_params.get('customerid'))
            if len(customer)!=0:
                i = customer[0]
                fields = {}
                fields['name'] = i.name
                fields['cid'] = i.cid.cid
                fields['nationality'] = i.nationality
                fields['type'] = i.type
                fields['phone_number']=str(i.phone_number)
                fields['email'] = i.email
                blist = []
                bookings = Booking.objects.filter(passengers=customer[0])
                for i in bookings:
                    passenger_list = []
                    passengers = i.passengers.all()
                    for j in passengers:
                        passenger_list.append(j.name)
                    blist.append(
                        {'airline':i.airline.name,
                        'pnr':i.pnr,
                        'flight_number':i.flight_number,
                        'sector':i.sector,
                        'flight_date':i.flight_date,
                        'flight_time':i.flight_time,
                        'passengers':passenger_list,
                        'expires_on':i.expires_on,
                        'class_name':i.class_name,
                        'booked_on':i.booked_on,
                        'ticketed':i.ticketed,
                        'nop':i.ticketed,
                        'unit_price':i.unit_price}
                    )
                fields['boookings'] = blist
                tlist = []
                tickets = Ticket.objects.filter(passenger_name=customer[0])
                for i in tickets:
                    tlist.append(
                        {'from_sector':i.from_sector,
                        'to_sector':i.to_sector,
                        'passenger_name':i.passenger_name.name,
                        'ticket_number':i.ticket_number,
                        'pnr':i.pnr,
                        'airlines':i.airlines.name,
                        'flight_date':i.flight_date,
                        'flight_time':i.flight_time,
                        'fare':str(i.fare),
                        'ticket_class':i.ticket_class,
                        'issued_at':i.issued_at}
                    )
                fields['tickets'] = tlist
                bllist=[]
                blls = Bill.objects.filter(ticket__passenger_name=customer[0])
                for i in blls:
                    bllist.append({'bill_number':i.bill_number,
                    'ticket':{'from_sector':i.ticket.from_sector,
                        'to_sector':i.ticket.to_sector,
                        'passenger_name':i.ticket.passenger_name.name,
                        'ticket_number':i.ticket.ticket_number,
                        'pnr':i.ticket.pnr,
                        'airlines':i.ticket.airlines.name,
                        'flight_date':i.ticket.flight_date,
                        'flight_time':i.ticket.flight_time,
                        'fare':str(i.ticket.fare),
                        'ticket_class':i.ticket.ticket_class,
                        'issued_at':i.ticket.issued_at},
                    'payment_received':i.payment_received})
                fields['bills'] = bllist

            else:
                fields = {}
                fields['name'] = None
                fields['cid'] = None
                fields['nationality'] = None
                fields['type'] = None
                fields['phone_number']=None
                fields['email'] = None
            return Response(fields)
        elif 'customer_name' in request.GET:
            customer = Customer.objects.filter(name=request.query_params.get('customer_name'))
            if len(customer)!=0:
                i = customer[0]
                fields = {}
                fields['name'] = i.name
                fields['cid'] = i.cid.cid
                fields['nationality'] = i.nationality
                fields['type'] = i.type
                fields['phone_number']=str(i.phone_number)
                fields['email'] = i.email
                blist = []
                bookings = Booking.objects.filter(passengers=customer[0])
                for i in bookings:
                    passenger_list = []
                    passengers = i.passengers.all()
                    for j in passengers:
                        passenger_list.append(j.name)
                    blist.append(
                        {'airline':i.airline.name,
                        'pnr':i.pnr,
                        'flight_number':i.flight_number,
                        'sector':i.sector,
                        'flight_date':i.flight_date,
                        'flight_time':i.flight_time,
                        'passengers':passenger_list,
                        'expires_on':i.expires_on,
                        'class_name':i.class_name,
                        'booked_on':i.booked_on,
                        'ticketed':i.ticketed,
                        
                        'nop':i.ticketed,
                        'unit_price':i.unit_price}
                    )
                fields['boookings'] = blist
                tlist = []
                tickets = Ticket.objects.filter(passenger_name=customer[0])
                for i in tickets:
                    tlist.append(
                        {'from_sector':i.from_sector,
                        'to_sector':i.to_sector,
                        'passenger_name':i.passenger_name.name,
                        'ticket_number':i.ticket_number,
                        'pnr':i.pnr,
                        'airlines':i.airlines.name,
                        'flight_date':i.flight_date,
                        'flight_time':i.flight_time,
                        'fare':str(i.fare),
                        'ticket_class':i.ticket_class,
                        'issued_at':i.issued_at}
                    )
                fields['tickets'] = tlist
                bllist=[]
                blls = Bill.objects.filter(ticket__passenger_name=customer[0])
                for i in blls:
                    bllist.append({'bill_number':i.bill_number,
                    'ticket':{'from_sector':i.ticket.from_sector,
                        'to_sector':i.ticket.to_sector,
                        'passenger_name':i.ticket.passenger_name.name,
                        'ticket_number':i.ticket.ticket_number,
                        'pnr':i.ticket.pnr,
                        'airlines':i.ticket.airlines.name,
                        'flight_date':i.ticket.flight_date,
                        'flight_time':i.ticket.flight_time,
                        'fare':str(i.ticket.fare),
                        'ticket_class':i.ticket.ticket_class,
                        'issued_at':i.ticket.issued_at},
                    'payment_received':i.payment_received})
                fields['bills'] = bllist
            else:
                fields = {}
                fields['name'] = None
                fields['cid'] = None
                fields['nationality'] = None
                fields['type'] = None
                fields['phone_number']=None
                fields['email'] = None

            return Response(fields)
    
    
    
        customers = Customer.objects.all()
        json = []
        for i in customers:
            fields = {}
            fields['name'] = i.name
            fields['cid'] = i.cid.cid
            fields['nationality'] = i.nationality
            fields['type'] = i.type
            fields['phone_number']=str(i.phone_number)
            fields['email'] = i.email
            json.append(fields)

        return Response(json)
    elif request.method == "POST":
        if request.POST.get("p_type") !=None:
            i = request.POST
            Customer.objects.create(name=i['passenger_name'],type=i['p_type'],nationality=i['nationality'],phonenumber=i['phonenumber'],email=i['email'])
            return Response({"status":"sucess"})
        return Response({"status":"failure"})

@api_view(['GET','POST','PUT'])
def bookings(request):
    if request.method == "GET":
        if "pnr" in request.GET:
            booking = Booking.objects.filter(pnr=request.query_params.get('pnr'))
            if len(booking)!=0:
                i = booking[0]
                fields = {}
                fields['airline'] = str(i.airline)
                fields['pnr'] = i.pnr
                fields['flight_number'] = i.flight_number
                fields['flight_date'] = i.flight_date
                fields['sector'] = i.sector
                passengers =[]
                for j in i.passengers.all():
                    passengers.append(j.name)
                fields['passengers']=passengers
                fields['expires_on'] = i.expires_on
                fields['class_name'] = i.class_name
                fields['booked_on'] = i.booked_on
                fields['ticketed'] = i.ticketed
                if fields['ticketed'] ==True:
                    fields['expires_on'] = ':'
                fields['nop'] = i.nop
                fields['unit_price'] = i.unit_price
            else:
                fields = {}
                fields['airline'] = None
                fields['pnr'] = None
                fields['flight_number'] = None
                fields['flight_date'] = None
                passengers =None
                fields['passengers']=passengers
                fields['expires_on'] = None
                fields['class_name'] = None
                fields['booked_on'] = None
                fields['ticketed'] = None
                fields['nop'] = None
                fields['unit_price'] = None
        
            return Response(fields)
    if request.method == "POST":
        if len(request.POST.get("passengers")) !=0:
            json = request.POST
            b = Booking()
            b.pnr = json['pnr']
            b.airline=Airline.objects.get(name=json['airline'])
            b.flight_number=json['flight_number']
            b.sector=json['sector']
            b.flight_date,b.flight_time=json['flight_date'],json['flight_time'].strip()
            if json['booked_on']:
                b.booked_on=json['booked_on']
            if json['ticketed']:
                b.ticketed=json['ticketed']
            b.nop=json['nop'] 
            b.unit_price=int(float(json['unit_price']))
            b.class_name=json['class_name']
            b.save()
            for i in json['passengers']:
                b.passengers.add(Customer.objects.get(name=i.strip()))


    bookings = Booking.objects.all()
    json = []
    for i in bookings:
        fields = {}
        fields['airline'] = str(i.airline)
        fields['pnr'] = i.pnr
        fields['flight_number'] = i.flight_number
        fields['flight_date'] = i.flight_date
        passengers =[]
        for j in i.passengers.all():
            passengers.append(j.name)
        fields['passengers']=passengers
        fields['expires_on'] = i.expires_on
        fields['class_name'] = i.class_name
        fields['booked_on'] = i.booked_on
        fields['ticketed'] = i.ticketed
        fields['nop'] = i.nop
        fields['unit_price'] = i.unit_price
        json.append(fields)

    return Response(json)

@api_view(['GET','POST'])
def tickets(request):
    if request.method == "GET":
        if "pnr" and "ticket_number" and "airline" in request.GET:
            try:
                tickets = Ticket.objects.filter(pnr=request.query_params.get('pnr'),ticket_number=request.query_params.get('ticket_number'),airlines=Airline.objects.filter(name=request.query_params.get('airline'))[0])
                
                i=tickets[0]
                fields = {}
                fields['airline'] = str(i.airlines)
                fields['pnr'] = i.pnr
                fields['flight_number'] = Booking.objects.get(pnr=i.pnr).flight_number
                fields['flight_date'] = i.flight_date
                fields['passenger_name']=i.passenger_name.name
                fields['ticket_number'] = i.ticket_number
                fields['class_name'] = i.ticket_class
                fields['isssued_at'] = i.issued_at
                fields['fare'] = str(i.fare)
                fields['FROM'] = i.from_sector
                fields['TO'] = i.to_sector
                fields['commission'] = str(Commission.objects.get(ticket=i).commission)
                
            except:
                fields = {}
                fields['airline'] = None
                fields['pnr'] = None
                fields['flight_number'] = None
                fields['flight_date'] = None
                fields['passenger_name']=None
                fields['ticket_number'] = None
                fields['class_name'] = None
                fields['isssued_at'] = None
                fields['fare'] = None
                fields['FROM'] = None
                fields['TO'] = None
                fields['commission'] = None
            return Response(fields)

            
        elif "pnr" in request.GET:
            tickets = Ticket.objects.filter(pnr=request.query_params.get('pnr'))
            json = []
            for i in tickets:
                fields = {}
                fields['airline'] = str(i.airlines)
                fields['pnr'] = i.pnr
                fields['flight_number'] = Booking.objects.get(pnr=i.pnr).flight_number
                fields['flight_date'] = i.flight_date
                fields['passenger_name']=i.passenger_name.name
                fields['ticket_number'] = i.ticket_number
                fields['class_name'] = i.ticket_class
                fields['isssued_at'] = i.issued_at
                fields['fare'] = str(i.fare)
                fields['FROM'] = i.from_sector
                fields['TO'] = i.to_sector
                fields['commission'] = str(Commission.objects.get(ticket=i).commission)
                json.append(fields)
            # return Response(json)
            return Response(json)


    tickets = Ticket.objects.all()
    json = []
    for i in tickets:
        fields = {}
        fields['airline'] = str(i.airlines)
        fields['pnr'] = i.pnr
        fields['flight_number'] = Booking.objects.get(pnr=i.pnr).flight_number
        fields['flight_date'] = i.flight_date
        fields['passenger_name']=i.passenger_name.name
        fields['ticket_number'] = i.ticket_number
        fields['class_name'] = i.ticket_class
        fields['isssued_at'] = i.issued_at
        fields['fare'] = str(i.fare)
        fields['FROM'] = i.from_sector
        fields['TO'] = i.to_sector
        fields['commission'] = str(Commission.objects.get(ticket=i).commission)
        json.append(fields)
    print(json)

    return Response(json)


def insert(response):
    return HttpResponse("Success")