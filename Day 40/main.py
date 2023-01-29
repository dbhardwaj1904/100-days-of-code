from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

print("Welcome to Flight Club, we find the best deals for you...")
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

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6*30)

for destination_code in destinations:
    flight = flight_search.check_flights(
        location,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]
        BODY = f"Low price alert -> from {flight.origin_city}, {flight.origin_airport}" \
               f" to {flight.destination}, {flight.destination_airport}"
        if flight.stop_overs > 0:
            BODY += f"flight has {flight.stop_overs}"
        link = "LINK FOR REDIRECTING"
        notification_manager.send_email(
            emails,
            BODY,
            link
        )
