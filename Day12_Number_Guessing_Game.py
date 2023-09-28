logo = '''
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"                                              
'''
import random
difficulty_level = [10, 5]
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")
    chosen_number = random.randint(1,100)

    difficulty_choice = input("Choose a difficulty. Type 'easy or 'hard: ").lower()
    while difficulty_choice not in ['easy', 'hard']:
        difficulty_choice = input("Invalid Choice Entered. Choose a difficulty. Type 'easy or 'hard: ").lower()


    no_of_guesses_left = difficulty_level[0] if difficulty_choice == 'easy' else difficulty_level[1]

    while no_of_guesses_left > 0:
        print(f"You have {no_of_guesses_left} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        no_of_guesses_left -= 1
        if guess == chosen_number:
            print(f"You are right! The number was {chosen_number}. You had {no_of_guesses_left} guesses left")
            break
        elif guess > chosen_number:
            print("Too high.")
        else:
            print("Too low.")

    if no_of_guesses_left==0:
        print(f"\nYou lost. The number was {chosen_number}")
    
    continue_playing = input("Enter 'yes' if you want to continue playing: ").lower()
    if continue_playing == 'yes':
        game()