#Create a math quiz program that asks the user to solve the addition of two random numbers
#If the user answers correctly, display that information
#Else, the program should display what the correct answer is

#import random module for generating random numbers
import random

#define main function
def main():
    #call the generate random function twice, assigning each of the returns to first and second num variables
    first_num = generate_random()
    second_num = generate_random()

    #call the add numbers function, passing first num and second num as arguments and assigning return value to added sum var
    added_sum = add_numbers(first_num, second_num)

    #call the prompt_user function passing the first and second num variables as arguments. Assign the return to given answer variable
    given_answer = prompt_user(first_num, second_num)

    #call the check answer function passing the sum of first and second num and the user provided answer as arguments
    check_answer(added_sum, given_answer)

#define the generate random function
def generate_random():
    #call the random int function from the random module, creating a random integer between 1 and 500
    #store that value in output num var
    output_num = random.randint(1, 500)

    #return output_num
    return output_num

#define the add numbers function with two parameters
def add_numbers(first_num, second_num):
    #return the sum of the two numbers passed into the function
    return first_num + second_num
        
#define the prompt user function with two parameters
def prompt_user(first_num, second_num):
    #prompt the user for the answer to the sum of the two parameters. Cast this answer as an int and store in user answer var
    user_answer = int(input(f"What is {first_num} + {second_num}? "))

    #return the user answer var
    return user_answer

#define check answer function with two parameters
def check_answer(correct_answer, given_answer):
    #if the correct answer is equal to the user provided answer
    if (correct_answer == given_answer):
        #print correct statement
        print("You are correct!")
    else: #else
        #print the correct answer
        print(f"Incorrect: the correct answer is {correct_answer}")

main()
