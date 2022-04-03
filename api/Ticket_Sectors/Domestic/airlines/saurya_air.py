import bs4
import requests
from .base import AirlineWebsite

class SauryaAir(AirlineWebsite):
    def __init__(self):
        base_url = "http://sauryaair.org/"
        super().__init__(base_url)
        self.cookies=self.get_cookies(self.session)

    def login(self,session):
        cookies = self.cookies
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://sauryaair.org',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://sauryaair.org/',
            'Accept-Language': 'en-US,en;q=0.9',
            }

        data = {
        'ipAddress': 'IpAddress',
        'clientOs': '',
        'macAddress': 'CPUId',
        'macAddress1': 'NetworkId',
        'requestFrom': 'Direct',
        'userId': 'antu',
        'password': 'ak330599'
        }

        response = session.post('http://sauryaair.org/Home/login.jsp', headers=headers, cookies=cookies, data=data, verify=False)

        headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://sauryaair.org/',
        'Accept-Language': 'en-US,en;q=0.9',
        }

        params = (
            ('LoginValidated', 'T'),
        )

        response = session.get('http://sauryaair.org/Home/login_sesuerity.jsp', headers=headers, params=params, cookies=cookies, verify=False)
        return session

    def re_login(self,session,response=False):
        headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://sauryaair.org/Home/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

        response = requests.get('http://sauryaair.org/SaOnlineReservation/loginagent.jsp', headers=headers, cookies=self.cookies, verify=False)

        headers = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://sauryaair.org/Home/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        params = (
            ('buddhaairreservationsessionid', '0098123GBcd0103023KKw'),
            ('ops', 'null'),
        )

        response = requests.get('http://sauryaair.org/SaOnlineReservation/login_sesuerity.jsp', headers=headers, params=params, cookies=self.cookies, verify=False)

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://sauryaair.org',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://sauryaair.org/SaOnlineReservation/main.jsp',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {
        'reconfirmusr': 'ANTU',
        'reconfirmpwd': 'ak330599',
        'confpwd': 'Confirm'
        }

        response = requests.post('http://sauryaair.org/SaOnlineReservation/rechkpwd.jsp', headers=headers, cookies=self.cookies, data=data, verify=False)
        return session

    def get_logged_in_session(self,response=False):
        log_1 = self.login(self.session)
        log_2 = self.re_login(log_1,response=response)
        
        return log_2

    def search_for_flights(self,ddd,mmm,yyy,fromsector,tosector):
        session = self.get_logged_in_session()
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://sauryaair.org',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://sauryaair.org/SaOnlineReservation/left.jsp',
            'Accept-Language': 'en-US,en;q=0.9',
        }


        params = (
            ('viewopt', 'view'),
        )

        data = {
        'ddd': ddd,
        'mmm': mmm,
        'yyy': yyy,
        'fromsector': fromsector,
        'tosector': tosector,
        'searchby': 'PNR',
        'searchval': ''
        }

        response = session.post('http://sauryaair.org/SaOnlineReservation/fdetail.jsp', headers=headers, params=params, cookies=self.cookies, data=data, verify=False).content
        soup = bs4.BeautifulSoup(response,'html.parser')
        self.session = session
        self.response,self.soup = response,soup
        self.js,self.flights = {},{}
        return self.response,self.soup

    def get_fares(self,fare="NPR"):
        fares = self.soup.find(id="fare")
        trs = fares.find_all('tr')
        for i in trs[3:]:
            a = i.find_all(['tr','td'])
           
            a=a[1:]
            if len(a)>10:
                self.js['SECTOR'] = a[0].get_text()
                    
                self.js[a[1].get_text()]=a[6].get_text()
                    

        return self.js
    def get_special_fares(self):
        soup = bs4.BeautifulSoup(self.response,'lxml')
        _class = soup.find_all(attrs={'class':'viewy'})
        _list=[]
        for i in _class:
            z = i.find_all("a")[0].get_text()
            j = i.find_all("td")[-1].get_text()
            if "Class" in j:
                dict = {'Flight number': z, 'Class': j.split()[1][1], 'New Fare': j.split()[3]}
                _list.append(dict)
        return _list
    
    def get_flight_and_seats(self):
        flights = self.soup.find_all(attrs={'class':'viewy'})
        for i in flights:
            j = i.a.find_all("td")
            self.flights[j[2].get_text()] = {}
            try:
                self.flights[j[2].get_text()]["N"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[3].get_text(),"Unit Price":self.get_fares()["N"],"Class":"N"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["O"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[4].get_text(),"Unit Price":self.get_fares()["O"],"Class":"O"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["P"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[5].get_text(),"Unit Price":self.get_fares()["P"],"Class":"P"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["Q"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[6].get_text(),"Unit Price":self.get_fares()["Q"],"Class":"Q"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["R"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[7].get_text(),"Unit Price":self.get_fares()["R"],"Class":"R"}
            except:
                pass
            try:
                self.flights[j[2].get_text()]["S"]={"Flight no.":i.a.get_text()[:6],"Number of seats available" : j[8].get_text(),"Unit Price":self.get_fares()["S"],"Class":"S"}
            except:
                pass
        
        self.flights_list=[]
        for i in self.flights:
            for j in self.flights[i]:
                time= f"{i[0:2]}:{i[2:]}"
                dict = {"Flight no.":self.flights[i][j]["Flight no."],"Class":self.flights[i][j]["Class"],"Time":time,"Maximum_Seats":self.flights[i][j]["Number of seats available"],"Unit_Price":self.flights[i][j]["Unit Price"]}
                self.flights_list.append(dict)
        improvise = self.get_special_fares()
        for i in improvise:
            for j in self.flights_list:
                if i["Flight number"] == j["Flight no."]:
                    if i["Class"]==j["Class"]:
                        j["Orignal_Price"] = j["Unit_Price"]
                        j["Unit_Price"]=i["New Fare"]
        self.flights_list={"Saurya Air":self.flights_list}
        return self.flights_list
    def get_referer(self,flight_number,class_name,nop):
        soup = bs4.BeautifulSoup(self.response,'html.parser')
        flights = soup.find_all(attrs={'class':'viewy'})
        cnt = len(flights)
        referer = 'http://sauryaair.org/SaOnlineReservation/main.jsp?'
        data = self.get_data(flight_number,class_name,nop)
        # print(data)
        for i in flights:
            au = str(i.font).split('<font color="#FFFFCC" face="Verdana, Arial, Helvetica, sans-serif">')[1].split('</font>')[0]
            referer+=f"&au{flights.index(i)+1}={au}&unid{flights.index(i)+1}={data[f'unid{flights.index(i)+1}']}&tt1=T"
        sector = i.font.find_all('td')[0].get_text()
        referer+=f"&cnt={cnt}&flt_date={data['fd1']}&sp={sector}"
        return referer
    def get_data(self,flight_number,class_name,nop):
        classes = {'N':'1','O':'2','P':'3','Q':'4','R':'5','S':'6'}
        class_name = classes[class_name]
        soup = bs4.BeautifulSoup(self.response,'lxml')
        flights = soup.find_all(attrs={'class':'viewy'})
        data={}
        flight_data={}
        for i in flights:
            flight_data[i.a.get_text()[:7]]={i.find(attrs={'name':f'unid{flights.index(i)+1}'})['name']:i.find(attrs={'name':f'unid{flights.index(i)+1}'})['value']}
            data[i.find(attrs={'name':f'fd{flights.index(i)+1}'})['name']]=i.find(attrs={'name':f'fd{flights.index(i)+1}'})['value']
            data[i.find(attrs={'name':f'unid{flights.index(i)+1}'})['name']]=i.find(attrs={'name':f'unid{flights.index(i)+1}'})['value']
            data[f'mclass{flights.index(i)+1}']='1'
            data[f'mpax{flights.index(i)+1}']=''
            data[f'open{flights.index(i)+1}']='F'
        # print(flight_data)
        flight_index= flight_data[flight_number]
        for i in flight_index:
            flight_index_ = ''
            for i in i:
                try:
                    i = int(i)
                    i = str(i)
                    flight_index_+=i
                except:
                    pass

        
        data[f'mclass{flight_index_}']=class_name
        data[f'mpax{flight_index_}']=nop
        data['proceed']= 'GO'
        data['valOft']= str(len(flights))
        data['cked']= ''
        data['munid']= flight_index[f'unid{flight_index_}']
        data['mclass']= class_name
        data['mopen']= ''
        data['mpax']= nop
        data['openbooking']= ''

        return data
    
    def individual_book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        self.search_for_flights(ddd,mmm,yyy,fromsector,tosector)
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://sauryaair.org',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        headers['Referer']=self.get_referer(flight_number,classname,nop)
        data = self.get_data(flight_number,classname,nop)
        response = self.session.post('http://sauryaair.org/SaOnlineReservation/reservation.jsp', headers=headers, data=data, verify=False)
        if "WE HAVE AN ERROR HERE" in response.content.decode():
            return {"status":"Error"}
        else:
            soup = bs4.BeautifulSoup(response.content.decode(),'lxml')

            json = {}
            json["status"] = "Success"
            json["Airline"] = "Saurya Air"
            json['PNR'] = soup.find(attrs={'class':'style1'}).get_text()[1:]
            json['BOOKING_EXPIRY']={}
            f = self.get_flight_and_seats()
            for i in f:
                for j in f[i]:
                    if j["Flight no."] == flight_number and j['Class']==classname:
                        json['TIME'] = j['Time']
                        json['flight_number'] = j["Flight no."]
                        json['Unit_Price'] = j['Unit_Price']
                        json['Class'] = j['Class']
                        # print(j['Time'])
                        break
            expiry = soup.find_all(attrs={'class':'style2'})
            # print(expiry)
            json['BOOKING_EXPIRY']['DATE'] = expiry[0].get_text()
            # print(json)
            time= f"{expiry[1].get_text()[0:2]}:{expiry[1].get_text()[2:]}"
            # print(time)
            json['BOOKING_EXPIRY']['TIME'] = time
            # print(json)
            # count+=1
            
            return json


