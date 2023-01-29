import requests

flightDeals = "GOOGLE_SHEETS_API"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.f_name = ""
        self.l_name = ""
        self.email = ""
        self.c_email = ""

    def user_details(self):
        self.f_name = input("Enter your first name?: ")
        self.l_name = input("Enter your last name?:")
        self.email = input("Enter your email?:")
        self.c_email = input("Confirm your email?:")

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

    def get_customer_emails(self):
        customers_endpoint = flightDeals
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
