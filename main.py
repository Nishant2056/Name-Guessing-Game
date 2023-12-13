import random

def guess_number():
    random_number = random.randint(1, 1000)
    max_attempts = 5
    attempts = 0
    print(f"Try to guess the number between 1 and 1000 You have {max_attempts} attempts to complete the game.")
    while attempts < max_attempts:
        try:
            manual_guess = int(input("Enter your guess: "))
            attempts += 1
            if manual_guess == random_number:
                print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
                break
            else:
                if manual_guess < random_number:
                    print("Try again! The number is higher.")
                else:
                    print("Try again! The number is lower.")
                print(f"You have {max_attempts - attempts} attempts remaining.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {random_number}.")
guess_number()