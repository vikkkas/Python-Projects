print(""" _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______     
|       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |    
|    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||    
|   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_   
|   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |  
|   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |  
|_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|  """)

#ASCII art generator http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

import random

print("Welcome to the number guessing game")

difficulty=input("Choose a difficluty. Type 'easy' or 'hard':")
if difficulty=="easy":
    lives = 10
else:
    lives = 5

number = random.randint(1,100)
print(number)

game_over = False
while not game_over:
    guess = int(input("Enter a Number:\n"))

    if guess>number:
        print("Too high guess")
        print("Guess again")
        print(f"You have {lives} attempts remaining to guess the number")
        lives -= 1

    elif guess<number:
        print("Too low guess")
        print("Guess again")
        print(f"You have {lives} attempts remaining to guess the number")
        lives-= 1

    else:
        print(f"You got it! The answer was {number}")
        break
    
    if lives==0:
        game_over=True
        print("You have run out of guesses. You Lose!!")  