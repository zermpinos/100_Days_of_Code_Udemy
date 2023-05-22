import os
from art import logo


def find_max_bidder(bidders_out):
    max_bid_in_1 = float('-inf')
    max_bidder_inner = None

    for bidder in bidders_out:
        bid_in_1 = bidder['bid_in_1']
        if bid_in_1 > max_bid_in_1:
            max_bid_in_1 = bid_in_1
            max_bidder_inner = bidder['name']

    return max_bidder_inner, max_bid_in_1


# Start
print('Welcome to the silent auction app!')
# Show logo
print(logo)

bidders = []

auction = True
while auction:
    name = input('Please give your name: \n')
    bid = int(input('Please give your bid: \n'))
    new_bid = {'name': name, 'bid': bid}
    bidders.append(new_bid)
    others = input('Are there others who want to bid? [Y]es or [N]o: \n').lower()
    if others == 'n':
        auction = False
    else:
        if os.name == 'nt':
            os.system('cls')  # Clear console on Windows
        else:
            os.system('clear')  # Clear console on macOS/Linux

max_bidder, max_bid = find_max_bidder(bidders)
print(f'The max bidder was {max_bidder} and betted {max_bid}')
