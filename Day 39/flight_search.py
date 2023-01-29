import requests
from flight_data import FlightData

tequila_endpoint = "TEQUILA_API_ENDPOINT"
tequila_apiKey = "TEQUILA_API"
location_types = "city"


class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = tequila_endpoint + "/locations/query"
        headers = {
            "apiKey": tequila_apiKey
        }
        query = {
            "term": city_name,
            "location_types": location_types
        }
        response = requests.get(location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "apiKey": tequila_apiKey
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strfttime("%d/%m/%Y"),
            "date_to": to_time.strfttime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopoevers": 0,
            "curr": "GBP"
        }

        response = requests.get(tequila_endpoint + "/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print("No flights found for" + destination_city_code)
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"]
        )
