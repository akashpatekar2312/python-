import random
import os

guess = []
init = 1
while init <= 100 :
    guess.append(init)
    init += 1
#print (guess)
computer_guess = random.choice(guess)
print (f"computer_number {computer_guess}")
print (type(computer_guess))



def guess_number():
    level = (input("Welcome to the Number Guessing Game...\nI am Thinking of number between 1 and 100 \nChoose a diffuculty type 'Easy' or 'Hard': ")).lower()
    if level == "easy" :
        tries = 10
        total_tries = 10
    elif level == "hard" :
        tries = 5
        total_tries = 5
    global is_game_over 
    is_game_over= False
    while not is_game_over :
        human_guess = int(input("Guess the number which you think that computer is thinking ...: "))
        #print (type(human_guess))
        if computer_guess == human_guess : 
            print("")
            print ("You Guessed it ...\nYou Won....!")
            is_game_over = True
        elif human_guess != computer_guess :
            tries -= 1
            print (f"You have {tries} chances left")
            if human_guess > computer_guess :
                os.system("cls")
                print (f"You have {tries} tries left")
                print ("Guess a smaller number")
            elif human_guess < computer_guess :
                os.system("cls")
                print (f"You have {tries} tries left")
                print ("Guess a bigger number")
                
            if tries == 0 :
                print("")
                print(f"Thinked number by the computer was : {computer_guess}")
                print (f"You didnt guessed the number in given {total_tries} tries\nYou loose....!")
                is_game_over = True
guess_number()

while (input("Do you want to play again ? : ")).lower() == "yes" :
    os.system("cls")
    guess_number()
