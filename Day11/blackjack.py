############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import os
os.system("cls")
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for drawn_card in range(2):
    user_cards.append(deal())
    computer_cards.append(deal())

print (user_cards)
print (computer_cards)

def calculate():
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    if user_score == 21 and len(user_cards) == 2 :
        user_core = 0
        print ("User has blackjack")
    elif computer_score == 21 and len(computer_cards) == 2 : 
        computer_score = 0
        print ("Computer has blackjack")

    if user_score > 21 and 11 in user_cards :
        user_cards.remove(11)
        user_cards.append(1)
    if computer_score > 21 and 11 in computer_cards : 
        computer_cards.remove(11)
        computer_cards.append(1)
    
        
    print (f"User's score is {user_score}")
    print (f"Computer's score is {computer_score}")
    print (f"Computer's first card is {computer_cards[0]}")
calculate()
