import json
from django.http.response import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .Ticket_Sectors.Domestic import main
from private.models import *
from private.serialiazers import *
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET'])
def domestic_search(request):
    date = request.query_params.get('date')
    dest = request.query_params.get('dest')
    MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
    yy = str(date[0:4])
    mm = str(date[5:7])
    dd = str(date[8:10])
    frm = str(dest[0:3])
    to =str(dest[4:])
    
    json = main.search_for_flights(dd,MONTHS[mm],yy,frm,to)
    return Response(json)

@api_view(['POST'])
def book_domestic_ticket(request):
    date = request.query_params.get('date')
    dest = request.query_params.get('dest')
    flight_number = request.query_params.get('f_no')
    classname = request.query_params.get('class')
    nop = request.query_params.get('nop')
    airline = request.query_params.get('airline')
    if airline in ["BA","SH","SA","YA","GA"]:

        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
        yy = str(date[0:4])
        mm = str(date[5:7])
        dd = str(date[8:10])
        frm = str(dest[0:3])
        to =str(dest[4:])

        return Response(main.airline_book(dd,MONTHS[mm],yy,frm,to,flight_number,classname,nop,airline))

    else:
        return Response({"status":"error"})

    
@api_view(['GET','POST','PUT','DELETE'])
def customer(request):
    if 'customerid' in request.GET:
        customerid = str(request.GET['customerid'])
        customer = Customer.objects.filter(cid__cid=customerid)
        if len(customer) == 1:
            customer = customer[0]
            json = CustomerSerializers(customer,many=False)
            if request.method == 'PUT':
                data = JSONParser().parse(request)
                serializer = CustomerSerializers(customer, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data)
                return Response(serializer.errors, status=400)
            return Response(json.data)
        else:
            json = CustomerSerializers(customer,many=False)
            return Response(json.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    

    else:
        customer = Customer.objects.all()
        json = CustomerSerializers(customer,many=True)
        return Response(json.data)

@api_view(['GET'])
def get_bills(request):
    # print(code)
    bills = Bill.objects.all()
    json = BillSerializers(bills,many=True)
    return Response(json.data)

@api_view(['GET'])
def get_all_bills_from_customer(request,customerid):
    # print(code)
    customer = Customer.objects.get(id=customerid)
    bills = customer.bills
    print(bills)
    json = BillSerializers(bills,many=True)
    return Response(json.data)


@api_view(['GET'])
def get_bill_from_customer(request,customerid,billid):
    customer = Customer.objects.get(id=customerid)
    bills = customer.bills.get(id=billid)
    print(bills)
    json = BillSerializers(bills)
    return Response(json.data)


@api_view(['GET'])
def get_all_tickets_from_customer(request,customerid):
    # print(code)
    customer = Customer.objects.get(id=customerid)
    bills = customer.ticket
    print(bills)
    json = TicketSerializers(bills,many=True)
    return Response(json.data)


@api_view(['GET'])
def get_ticket_from_customer(request,customerid,ticketid):
    customer = Customer.objects.get(id=customerid)
    bills = customer.ticket.get(id=ticketid)
    print(bills)
    json = TicketSerializers(bills)
    return Response(json.data)

@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    json = BookingSerializers(bookings,many=True)
    return Response(json.data)

@api_view(['GET'])
def get_bookings_by_pnr(request,pnr):
    if Booking.objects.filter(pnr=pnr).count()>0:
        bookings = Booking.objects.get(pnr=pnr)
        json = BookingSerializers(bookings)
        return Response(json.data)
    else:
        return HttpResponse('No bookings')