#Blackjack game first attempt
import random
# def blackjack():
#     values = [1,2,3,4,5,6,7,8,9,10,'jack','queen','king','ace']
#     bidder_count = 0
#     dealer_count = 0
#     first_card = random.choices(values)
#     second_card = random.choices(values)
#     third_card = random.choices(values)
#     fourth_card = random.choices(values)
#     dealer_card_1 = random.choices(values)
#     dealer_card_2 = random.choices(values)
#     dealer_card_3 = random.choices(values)
#     dealer_card_4 = random.choices(values)
#     print(f"Your cards are:{first_card} and {second_card}" )
#     print(f"The dealer's first card are:{dealer_card_1}\n" )
#     hit_or_stay = input("Would you like to 'hit' or 'stay'?\n")
#     if first_card == ['jack'] or ['queen'] or ['king']:
#         first_card = 10
#     elif second_card == ['jack'] or ['queen'] or ['king']:
#         second_card = 10

#     bidder_count = bidder_count + first_card + second_card
#     if hit_or_stay == 'hit':
#         if third_card == ['jack'] or ['queen'] or ['king']:
#             third_card = 10
#         bidder_count = bidder_count + third_card
#         print(f"Your third card is {third_card}\n and your total is {bidder_count} and the dealers total is: {dealer_count}")
#     elif hit_or_stay == 'stay':
#         print(f"Your total is: {bidder_count} and the dealers total is: {dealer_count}")


# blackjack()

#ChatGPT Solution
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 = J, Q, K; 11 = Ace
#     return random.choice(cards)

# def calculate_score(cards):
#     """Calculate the score of the hand."""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0  # Blackjack
#     if 11 in cards and sum(cards) > 21:
#         cards[cards.index(11)] = 1
#     return sum(cards)

# def compare(player_score, dealer_score):
#     if player_score == dealer_score:
#         return "Draw!"
#     elif dealer_score == 0:
#         return "Lose, dealer has Blackjack!"
#     elif player_score == 0:
#         return "Win with a Blackjack!"
#     elif player_score > 21:
#         return "You went over. You lose!"
#     elif dealer_score > 21:
#         return "Dealer went over. You win!"
#     elif player_score > dealer_score:
#         return "You win!"
#     else:
#         return "You lose!"
    
# def play_game():
#     print("=== Welcome to Blackjack ===")

#     player_cards = [deal_card(), deal_card()]
#     dealer_cards = [deal_card(), deal_card()]

#     game_over = False

#     while not game_over:
#         player_score = calculate_score(player_cards)
#         dealer_score = calculate_score(dealer_cards)

#         print(f"Your cards: {player_cards}, current score: {player_score}")
#         print(f"Dealer's first card: {dealer_cards[0]}")

#         if player_score == 0 or dealer_score == 0 or player_score > 21:
#             game_over = True
#         else:
#             should_continue = input("Type 'y' to get another card, 'n' to pass: ")
#             if should_continue == 'y':
#                 player_cards.append(deal_card())
#             else:
#                 game_over = True

#     while dealer_score != 0 and dealer_score < 17:
#         dealer_cards.append(deal_card())
#         dealer_score = calculate_score(dealer_cards)

#     print(f"\nYour final hand: {player_cards}, final score: {player_score}")
#     print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
#     print(compare(player_score, dealer_score))

# while input("Play a game of Blackjack? (y/n): ") == "y":
#     play_game()

def card_draw():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,11]
    return random.choice(cards)