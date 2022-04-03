import requests
from requests_html import HTMLSession

class AirlineWebsite():
    def __init__(self,base_url):
        self.BASE_URL = base_url
        self.session = requests.Session()
        self.HTMLsession = HTMLSession()

    def get_cookies(self,session):
        cookies = session.get(self.BASE_URL).cookies.get_dict()
        return cookies

    def base_login(self,response=False):
        session= self.get_logged_in_session(response)
        return session

    def get_balance(self):
        self.balance = self.check_balance_individually()
        return self.balance

    def search_flights(self,ddd,mmm,yyy,fromsector,tosector,passenger_count=1):
        self.search_for_flights(ddd,mmm,yyy,fromsector,tosector)
        json = self.get_flight_and_seats()
        return json

    # def book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        
        
    def book(self,ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop):
        return self.individual_book(ddd,mmm,yyy,fromsector,tosector,flight_number,classname,nop)
