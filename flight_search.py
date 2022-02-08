import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


class FlightSearch:
    def __init__(self):
        self.token = TOKEN
        self.endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.fly_from = "GSO,RDU,CLT",
        self.fly_to = "",
        self.date_from = "",
        self.date_to = ""

    def get_flights(self, date_to, date_from, iata_code):
        price_list = []
        for code in iata_code:
            header = {
                "apikey": self.token
            }
            params = {
                "fly_from": self.fly_from,
                "fly_to": code,
                "date_from": date_to,
                "date_to": date_from,
                "curr": "GBP",
                "one_for_city": "1",
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 10
            }
            response = requests.get(url=self.endpoint, headers=header, params=params)

            data = response.json()["data"]
            for flight in data:
                price_list.append({"city": flight["cityTo"], "price": int(flight["price"]), "from": flight["flyFrom"]})
        return price_list

    def get_codes(self, term):
        endpoint = "https://tequila-api.kiwi.com/locations/query"
        header = {
            "apikey": self.token
        }
        params = {
            "term": term
        }
        response = requests.get(url=endpoint, headers=header, params=params)
        data = response.json()
        return data



