logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import os
clear= lambda : os.system('cls')

def deal_card():
    import random   
    """" Returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_chosen = random.choice(cards)
    return card_chosen


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
#blackjack check
#blackjack (a hand with only 2 cards: ace + 10)

    if sum(cards)==21 and len(cards):
    #if 11 in computer_card and 10 in computer_card and len(computer_card)==2:
        return 0
    #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove()
    if 11 in cards and sum(cards)>21:
        cards.remove(21)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw😐"
    elif computer_score == 0 :
        return "Lose, Opponent has a blackjack 😱 "
    elif user_score==0:
        return "Win with a blackjack 😎 "
    elif user_score>21:
        return "You went over. You Lose 😭"
    elif computer_score>21:
        return "Computer went over. You win 😁"
    elif user_score > computer_score :
        return "You Win 😊"
    else:
        return "You Lose 😭"
def play_game():

    print(logo)
    user_card = []
    computer_card = []
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, Current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while not computer_score != 0 and computer_score < 17 :
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
        
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")

    print(compare(user_score,computer_score))


#Execution
play_game()

#Repeatition
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()