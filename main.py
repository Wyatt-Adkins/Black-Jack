from art import logo
import os
import random
def clear():
    """Clears the console across Operating Systems"""

    command = 'clear'
  
    if os.name in ('nt', 'dos'):
        command = 'cls'
    
    os.system(command)

def deal_card():
   
    """Returns a random car from the deck"""
  
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
  
    card = random.choice(cards)
   
    return card


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
  
    if sum(cards) == 21 and len(cards) == 2: 
        return 0 
 
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
   
    return sum(cards)

def compare(user_score, computer_score): 
    """Pass in both the user's score and the computer's as arguments"""
    # lose/win condition statements 

    if user_score == computer_score:
        return "Draw"
    
    elif computer_score == 0:
        return "Lose, I has Blackjack!"
    
    elif user_score == 0: 
        return "Win with a Blackjack! cheater!"
 
    elif user_score > 21:
        return "YOU BUST. You lose :)"
   
    elif computer_score > 21: 
        return "I BUST. You win."
   
    elif user_score > computer_score:
        return "You win! congrats human."
    
    else:
        return "You LOSE :)"

def playgame():
    """This function will be run so the game begins"""

    print(logo)

   
    user_cards = []
    computer_cards = []

 
    is_game_over = False
  
    for _ in range(2):

        user_cards.append(deal_card())
        computer_cards.append(deal_card())
  
    while not is_game_over: 

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]} \n")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card()) 
            else: 
                is_game_over = True 
    while computer_score != 0 and computer_score < 17: 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        # final hand
    print(f"Your final hand: {user_cards}, your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Want to play Blackjack? Type 'y' to start, hit enter to leave: "):
#    clear screen
    clear()
#   game over
    playgame()