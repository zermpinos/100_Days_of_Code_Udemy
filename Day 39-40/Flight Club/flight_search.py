import os
import requests
from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    @staticmethod
    def get_destination_codes(cities):
        city_codes = []
        for city in cities:
            response = requests.get(
                f"{TEQUILA_ENDPOINT}/locations/query",
                headers={"apikey": TEQUILA_API_KEY},
                params={"term": city, "location_types": "city"}
            )
            result = response.json()["locations"]
            city_codes.append({"id": result[0]["id"], "iataCode": result[0]["code"]})
        return city_codes

    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_time, to_time):
        response = requests.get(
            f"{TEQUILA_ENDPOINT}/v2/search",
            headers={"apikey": TEQUILA_API_KEY},
            params={
                "fly_from": origin_city_code,
                "fly_to": destination_city_code,
                "date_from": from_time.strftime("%d/%m/%Y"),
                "date_to": to_time.strftime("%d/%m/%Y"),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 2,
                "curr": "GBP"
            }
        )

        try:
            data = response.json()["data"][0]
            flight_data = FlightData(data)
            return flight_data
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
