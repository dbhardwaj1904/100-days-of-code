import requests

flightDeals = "GOOGLE_SHEETS_API"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(flightDeals)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self, code):
        for city in self.destination_data:
            params = {
                "price": {
                    "iataCode": code
                }
            }
            response = requests.put(flightDeals + "/" + str(city["id"]), json=params)
            print(response.json())
