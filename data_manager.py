import requests
import os
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")


class DataManager:
    def __init__(self):
        self.auth = (USER, PASSWORD)
        self.endpoint = ""

    def get_data(self):
        self.endpoint = "https://api.sheety.co/f1d4d46bfaa887c14bc9043c594ef651/flightDeals/sheet1"
        response = requests.get(url=self.endpoint, auth=self.auth)
        data = response.json()
        return data

    def add_iata_code(self, row_id):
        self.endpoint = f"https://api.sheety.co/f1d4d46bfaa887c14bc9043c594ef651/flightDeals/sheet1/{row_id}"
        data = {
            "sheet1": {
                "iata code": "test"
            }
        }
        response = requests.put(url=self.endpoint, auth=self.auth, json=data)
        print(response.status_code)
        print(response.text)
