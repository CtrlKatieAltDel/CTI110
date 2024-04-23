#KATIE ELDER

#04/23/2024

#P5HW

#A math quiz program where the user can choose between adding or subtracting random numbers, and the program provides feedback based on the user's guesses.


import random

def generate_numbers():
    return random.randint(100, 999), random.randint(100, 999)
# Allows the user to guess the sum of two random numbers/providing feedback based on whether the guess is correct, too low, or too high.
def add_quiz():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guesses = 0
#This starts an infinite loop where the user can make guesses.
    while True:
        print("   ", num1)
        print("+ ", num2)
        guess = int(input("Enter answer: "))
#Guesses counter to keep track of the number of guesses.
        guesses += 1
# This checks if the user's guess matches the correct answer.
        if guess == correct_answer:
            print("Congratulations! Your answer is correct.")
            print("Number of guesses:", guesses)
            break
# If the guess is less than the correct answer, it notifies the user that their guess is too low and prompts them to try again.
        elif guess < correct_answer:
            print("Sorry, your guess is too low. Try again.")
#This notifies the user that their guess is too high
        else:
            print("Sorry, your guess is too high. Try again.")

def subtract_quiz():
#This line generates two random numbers
    num1, num2 = generate_numbers()
#This calculates the correct answer
    correct_answer = num1 - num2
#Keeps track of the number of guesses
    guesses = 0
#This starts an infinite loop where the user can make guesses until they guess the correct answer
    while True:
        print("   ", num1)
        print("- ", num2)
        guess = int(input("Enter answer: "))
        guesses += 1
        if guess == correct_answer:
            print("Congratulations! Your answer is correct.")
            print("Number of guesses:", guesses)
            break
        elif guess < correct_answer:
            print("Sorry, your guess is too low. Try again.")
        else:
            print("Sorry, your guess is too high. Try again.")

def main():
    print("Welcome to Math Quiz\n")
#Loop to display the main menu and prompt the user for their choice.
    while True:
        print(" MAIN MENU")
        print("-------------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        choice = input("Please choose one of the menu options: ")

        if choice == '1':
            add_quiz()
        elif choice == '2':
            subtract_quiz()
        elif choice == '3':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
