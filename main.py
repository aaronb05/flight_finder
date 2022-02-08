import flight_search
import flight_data
import data_manager
import notification_manager
import datetime
import pandas

# CREATE CLASSES
flight_data = flight_data.FlightData()
flight_search = flight_search.FlightSearch()
data_manager = data_manager.DataManager()
notification_manager = notification_manager.NotificationManager()

# GET LIST OF AIRPORT CODES FROM CSV #
iata_codes_list = []
# GET GOOGLE DATA
google_data = data_manager.get_data()["sheet1"]
print(google_data)
# for city in google_data:
#     term = city['city']
#     code = flight_search.get_codes(term)["locations"][0]["code"]
#     iata_codes_list.append(code)
#     data_manager.add_iata_code(row_id=2)
flight_csv = pandas.read_csv("FlightDeals.csv")
for code in flight_csv["IATA Code"]:
    iata_codes_list.append(code)

# GET LIST OF DICTIONARIES OF ALL FLIGHTS AND PRICES TO EVERY LOCATION IN LIST
current_date = datetime.datetime.now()
date_to = current_date + datetime.timedelta(days=180)
flight_data = flight_search.get_flights(date_to=current_date.strftime("%d/%m/%Y"),
                                        date_from=date_to.strftime("%d/%m/%Y"), iata_code=iata_codes_list)
flight_details = {row["City"]: row["Lowest Price"] for (index, row) in flight_csv.iterrows()}
# COMPARE SET PRICE TO CURRENT FLIGHTS AND SEE IF THERE ARE ANY CHEAPER THAN SET PRICE
# IF THERE ARE THEN LET USER KNOW VIA SMS ALERT
for city in flight_details:
    target_city = city
    target_price = flight_details[city]
    for num in range(len(flight_data)):
        if city == flight_data[num]["city"]:
            flight_price = flight_data[num]["price"]
            if flight_price < target_price:
                departing_airport = flight_data[num]["from"]
                print(f"Flights to {target_city} from {departing_airport} have dropped "
                      f"below {target_price} to {flight_price}. "
                      f"Go check out flights to {target_city}!")
            else:
                print(f"No cheap flights to {target_city}")


