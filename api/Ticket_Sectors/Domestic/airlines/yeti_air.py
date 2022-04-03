
from http import cookies
import bs4
import requests
from .base import AirlineWebsite



class YetiAir(AirlineWebsite):
    def __init__(self):
        base_url = "http://res.yetiairlines.com/b2b/"
        super().__init__(base_url)
        self.cookies=self.get_cookies(self.session)

    def login(self):
        cookies = cookies = {
           'ASP.NET_SessionId': 'xwktbbyturyeoc45g2duoz45',
}
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"userName":"antu","PassWord":"Aaryan330599","companyname":"antu"}'

        session = requests.Session()
        response = session.post('http://res.yetiairlines.com/b2b/WebService/BaseService.asmx/UserLogOn', headers=headers, cookies=cookies, data=data, verify=False)
        

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=cookies, verify=False)

        return session
    
    def get_logged_in_session(self,response=False):
        log_1 = self.login()
        
        return log_1


    def search_for_flights(self,ddd,mmm,yyy,fromsector,tosector,passenger_count=1):
        session = self.get_logged_in_session()
        cookies = cookies = {
                    'ASP.NET_SessionId': 'xwktbbyturyeoc45g2duoz45',
                }
        yy= yyy
        mm=mmm
        MONTHS = {"01":"JAN","02":"FEB","03":"MAR","04":"APR","05":"MAY","06":"JUN","07":"JUL","08":"AUG","09":"SEP","10":"OCT","11":"NOV","12":"DEC"}
        for i in MONTHS:
            if MONTHS[i] == mm:
                mm = i
        dd = ddd
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"fromAirport":"KTM","toAirport":"BDP","dateFrom":"20211005","dateTo":"","iAdult":"1","iChild":"0","iInfant":"0","BDClass":"","isSearchGroup":"0","FareSelect":"","dayRange":"0","transit_flag":"false","direct_flag":"true","require_passenger_title_flag":"false","require_passenger_gender_flag":"false","require_date_of_birth_flag":"true","require_document_details_flag":"true","require_passenger_weight_flag":"false","OriginName":"Kathmandu","DestinationName":"Bhadrapur","show_redress_number_flag":"true","special_service_fee_flag":"true","currency":"NPR","bNoVat":false,"strPromoCode":"","strIPAddress":"","iOther":0,"otherPassengerTypeCode":""}'
        import json
        data = json.loads(data)
        data["toAirport"]=tosector
        data["fromAirport"]=fromsector
        data["dateFrom"]=f"{yy}{mm}{dd}"
        data["iAdult"]=passenger_count
        data = json.dumps(data)
        response = session.post('http://res.yetiairlines.com/b2b/WebService/BaseService.asmx/getFlightAvailabilityFormMultiCurrency', headers=headers, cookies=cookies, data=data, verify=False)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': '*/*',
            'Origin': 'http://res.yetiairlines.com',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = '{"move":"next"}'

        response = session.post('http://res.yetiairlines.com/b2b/WebService/UtilService.asmx/GetNextWorkFlowStep', headers=headers, cookies=cookies, data=data, verify=False)

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://res.yetiairlines.com/b2b/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = session.get('http://res.yetiairlines.com/b2b/', headers=headers, cookies=cookies, verify=False)
        soup = bs4.BeautifulSoup(response.content,'html.parser')
        self.soup = soup
        self.js = {}
        self.flights={}
        return response.content
        

    def get_flight_and_seats(self,fare="NPR"):
        table = self.soup.find(id="tabOutward")
        trs = table.find_all(['tr','tbody'])
        trs = trs[:-1]
        trs=trs[1:]
        flight_name = ""
        new_list = []
        for i in trs:
            td = i.find_all("td")
            if "YT" in td[0].get_text():
                flight_name = td[0]
                new_list.append(td)
            else:
                td[0]=flight_name
                new_list.append(td)
        self.flights_list=[]
        for i in new_list:
            fare = i[8].get_text()
            fare = fare.split(",")
            fare = fare[0]+fare[1]
            fare = fare.split(".")
            if int(fare[1])>1:
                fare = int(fare[0])+1
            else:
                fare = fare[0]
            dict = {"Flight no.":f"{i[0].get_text()[0:2]} {i[0].get_text()[26:29]}","Class":i[6].get_text(),"Time":i[3].get_text(),"Maximum_Seats":i[7].get_text(),"Unit_Price":fare}
            self.flights_list.append(dict)
        self.flights_list={"Yeti Airlines":self.flights_list}
        return self.flights_list


