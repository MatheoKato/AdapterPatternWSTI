import requests
import json

class GoldService():
    def __init__(self, ):
        self.url = 'http://api.nbp.pl/api/cenyzlota/today/?format=json'
        self.req = requests.get(self.url)

    def get_price(self):
        if self.req.status_code != requests.codes.ok:
            print("Nie ma ceny złota z dzisiejszego dnia, proszę sprawdź jutro")
        else:
            print(json.dumps(self.req.json()))



