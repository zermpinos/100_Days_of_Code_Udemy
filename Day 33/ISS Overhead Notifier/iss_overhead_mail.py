import os
import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
import math

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
MY_LAT = 00.000000  # Your latitude
MY_LONG = 00.000000  # Your longitude
MY_SMTP_ADDRESS = os.getenv("MY_SMTP_ADDRESS")


def is_iss_overhead(iss_lat, iss_lon, my_latitude, my_longitude):
    if my_latitude-5 <= iss_lat <= my_latitude+5 and my_longitude-5 <= iss_lon <= my_longitude+5:
        print("ISS is overhead.")
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        print("It's night time.")
        return True


def calculate_distance(lat1, lon1, lat2, lon2):
    r = 6371  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c

    return distance


def get_iss_updates(my_latitude, my_longitude):
    while True:
        time.sleep(600)

        # Get the current ISS position
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()
        iss_data = iss_response.json()

        iss_lat = float(iss_data["iss_position"]["latitude"])
        iss_lon = float(iss_data["iss_position"]["longitude"])

        # Calculate the distance between ISS and your location
        distance_to_iss = calculate_distance(my_latitude, my_longitude, iss_lat, iss_lon)
        print(f"Current distance to ISS: {distance_to_iss:.2f} km")

        if is_iss_overhead(iss_lat, iss_lon, my_latitude, my_longitude) and is_night():
            try:
                connection = smtplib.SMTP(MY_SMTP_ADDRESS)
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Look Up👆\n\nThe ISS is above you in the sky."
                )
                print("Email sent successfully.")
            except Exception as e:
                print(f"Error sending email: {e}")


# Call the function with your location
get_iss_updates(MY_LAT, MY_LONG)
