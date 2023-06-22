import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


class DataManager:
    def __init__(self):
        self.city_codes = []

    @staticmethod
    def get_destination_data():
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        response = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        return data["prices"]

    def update_destination_codes(self):
        for city_code in self.city_codes:
            new_data = {
                "price": {
                    "iataCode": city_code["iataCode"]
                }
            }
            headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
            response = requests.put(
                f"{SHEETY_PRICES_ENDPOINT}/{city_code['id']}",
                json=new_data,
                headers=headers
            )

    @staticmethod
    def get_customer_emails():
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
        response = requests.get(SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        return data["users"]
