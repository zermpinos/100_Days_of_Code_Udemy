from art import logo
import random
import replit

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 21:
        return "Computer has a blackjack! You lose."
    elif user_score == 21:
        return "You have a blackjack! You win."
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

while input("Do you want to play a game of blackjack? 'y' or 'n': ").lower() == 'y':
    replit.clear()
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_hand = [deal_card(), deal_card()]
    player_hand = [deal_card(), deal_card()]

    game_over = False
    while not game_over:
        user_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 21 or computer_score == 21 or user_score > 21:
            game_over = True
        else:
            another_card = input("Do you want to draw another card? 'y' or 'n': ").lower()
            if another_card == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))
