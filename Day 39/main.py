from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

location = "LON"

sheet_data = data_manager.get_destination_data()
if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6*30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        location,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    BODY = f"Low price alert from {flight.origin_city}, {flight.origin_airport}" \
           f" to {flight.destination}, {flight.destination_airport}"
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=BODY
        )
