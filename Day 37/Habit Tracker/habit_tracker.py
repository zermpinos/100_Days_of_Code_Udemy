import requests
from datetime import datetime
import os

USERNAME = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def add_pixel(quantity):
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now()
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

def update_pixel(quantity, date):
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    new_pixel_data = {
        "quantity": quantity
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

def delete_pixel(date):
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)


# Uncomment the following lines to create a user and graph
# create_user()
# create_graph()

# Add a new pixel
quantity = input("How many kilometers did you cycle today? ")
add_pixel(quantity)

# Update or delete a pixel
# update_pixel("4.5", "20210621")
# delete_pixel("20210621")

# You can store your credentials in environment variables by adding the following lines to your .bashrc or .bash_profile file
# export PIXELA_USERNAME="YOUR USERNAME"
# export PIXELA_TOKEN="YOUR SELF GENERATED TOKEN"

# Don't forget to restart your terminal or run source ~/.bashrc or source ~/.bash_profile after adding these lines.
