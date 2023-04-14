#Create a random number guessing game that asks the player to guess a random number between 1 and 100
#If number guessed is not equal to number generated, program should respond in what direction (high or low) player's guess was and to guess again
#If number guessed is equal, program should congradulate player and generate another number to guess

import random

def main():
    player_guessed_number = ""

    random_number = generate_number()

    print("Random Number Guessing Game!")

    player_guessed_number = take_guess()

    check_answer(random_number, player_guessed_number)
    

def generate_number():
    RANDOM_FLOOR = 1
    RANDOM_CEILING = 100

    generated_number = random.randint(RANDOM_FLOOR, RANDOM_CEILING)

    return generated_number

def take_guess():
    player_guessed_number = int(input("Enter an integer between 1 and 100 inclusive: "))

    return player_guessed_number

def check_answer(generated_number, guessed_number):

    while guessed_number != generated_number:
        
        if guessed_number > generated_number:
            print("Too High!")
        else:
            print("Too Low!")
        
        guessed_number = take_guess()
            

    print(f"Correct! You answered {generated_number}")

main()