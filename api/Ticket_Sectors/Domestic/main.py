from .airlines import buddha_air,yeti_air,guna_air,saurya_air,shree_air
import concurrent.futures
import datetime



def execute(func,args=None):
    with concurrent.futures.ThreadPoolExecutor as executor:
        f1=executor.submit(func,args)
        return f1.result()


def fetch_buddha_air(dd,mm,yy,fromsector,tosector):
    try:
        json = buddha_air.BuddhaAir().search_flights(dd,mm,yy,fromsector,tosector)
        json["status"] = "success"
        return json
    except:
        return {}

def fetch_shree_air(dd,mm,yy,fromsector,tosector):
    try:
        json = shree_air.ShreeAir().search_flights(dd,mm,yy,fromsector,tosector)
        json["status"] = "success"
        return json
    except:
        return {}


def fetch_yeti_airlines(dd,mm,yy,fromsector,tosector,passenger_count=1):
    try:
        json = yeti_air.YetiAir().search_flights(dd,mm,yy,fromsector,tosector,passenger_count)
        json["status"] = "success"
        return json
    except:
        return {}


def fetch_saurya_airlines(dd,mm,yy,fromsector,tosector,passenger_count=1):
    try:
        json = saurya_air.SauryaAir().search_flights(dd,mm,yy,fromsector,tosector,passenger_count)
        json["status"] = "success"
        return json
    except:
        return {}

def fetch_guna_airlines(dd,mm,yy,fromsector,tosector,passenger_count=1):
    try:
        json = guna_air.GunaAir().search_flights(dd,mm,yy,fromsector,tosector,passenger_count)
        json["status"] = "success"
        return json
    except:
        return {}



def time_sort(list):
    # list = [{'Airline': 'Buddha Air', 'Time': '07:00  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '07:00  ', 'Maximum_Seats': '01', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '09:40  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '09:40  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '12:30  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '12:30  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '15:35  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '15:35  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Buddha Air', 'Time': '17:25  ', 'Maximum_Seats': '07', 'Unit_Price': '9530'}, {'Airline': 'Buddha Air', 'Time': '17:25  ', 'Maximum_Seats': '03', 'Unit_Price': '8330'}, {'Airline': 'Shree Air', 'Time': '11:00  ', 'Maximum_Seats': '08', 'Unit_Price': '9600'}, {'Airline': 'Shree Air', 'Time': '11:00  ', 'Maximum_Seats': '05', 'Unit_Price': '8400'}, {'Airline': 'Shree Air', 'Time': '17:00  ', 'Maximum_Seats': '08', 'Unit_Price': '9600'}, {'Airline': 'Shree Air', 'Time': '17:00  ', 'Maximum_Seats': '01', 'Unit_Price': '8400'}]
    for i in list:
        i["Time"]=i["Time"][0:2]+i["Time"][3:5]
    
    money_list=[]
    for i in list:
        money_list.append(i['Time'])

    time_list = sorted(set(money_list))
    final_list=[]
    for i in time_list:
        for j in list:
            if j["Time"] == i:
                final_list.append(j)

    for i in final_list:
        i["Time"]= i["Time"][0:2]+":"+i["Time"][2:]

    return final_list


def search_for_flights(dd,mm,yy,fromsector,tosector):
    final_dict={}
    executor = concurrent.futures.ThreadPoolExecutor()
    buddha_air = executor.submit(fetch_buddha_air,dd,mm,yy,fromsector,tosector).result()
    shree_air=executor.submit(fetch_shree_air,dd,mm,yy,fromsector,tosector).result()
    yeti_airlines=executor.submit(fetch_yeti_airlines,dd,mm,yy,fromsector,tosector).result()
    saurya_airlines = executor.submit(fetch_saurya_airlines,dd,mm,yy,fromsector,tosector).result()
    guna_airlines = executor.submit(fetch_guna_airlines,dd,mm,yy,fromsector,tosector).result()

    # print(shree_air)
    for i in buddha_air:
        final_dict[i] = buddha_air[i]
    for i in shree_air:
        final_dict[i] = shree_air[i]
    for i in yeti_airlines:
        final_dict[i] = yeti_airlines[i]
    for i in saurya_airlines:
        final_dict[i] = saurya_airlines[i]
    for i in guna_airlines:
        final_dict[i] = guna_airlines[i]
    # final_dict=time_sort(final_dict)
    return final_dict

def fetch_offers(fromsector,tosector):
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
    offer_json = {}
    json = search_for_flights(day,MONTHS[month],year,fromsector,tosector)
    sectors = ["BDP","BHR","BIR","BWA","CCU","DHI","JKR","KEP","KTM","MTN","PKR","RJB","SIF","SKH","TMI"]


    # MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}


def airline_book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop,airlines):
    if airlines=="SH":
        return shree_air.ShreeAir().book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
    elif airlines=="BA":
        return buddha_air.BuddhaAir().book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
    elif airlines=="SA":
        return saurya_air.SauryaAir().book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
    elif airlines=="YA":
        return yeti_air.YetiAir().book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
    elif airlines=="GA":
        return guna_air.GunaAir().book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
    else:
        return {"status":"error","desc":"no such airline"}



