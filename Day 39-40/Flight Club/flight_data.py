class FlightData:
    def __init__(self, data):
        self.price = data["price"]
        self.origin_city = data["route"][0]["cityFrom"]
        self.origin_airport = data["route"][0]["flyFrom"]
        self.destination_city = data["route"][0]["cityTo"]
        self.destination_airport = data["route"][0]["flyTo"]
        self.out_date = data["route"][0]["local_departure"].split("T")[0]
        self.return_date = data["route"][-1]["local_departure"].split("T")[0]
        self.stop_overs = len(data["route"]) - 2
        self.via_city = ""
        if self.stop_overs > 0:
            self.via_city = data["route"][1]["cityFrom"]
