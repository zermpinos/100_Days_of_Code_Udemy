# DO NOT MODIFY THIS FILE

class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when the payment is accepted, or False if insufficient."""
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False
