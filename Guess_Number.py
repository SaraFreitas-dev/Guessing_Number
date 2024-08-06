import random
from img.images import logo_ascii, win_ascii, loose_ascii

def start_game():
    print(logo_ascii)
    print("\033[1mWelcome  to the Number Guessing Game !\nI'm thinking of a Number from 1 to 100.\033[0m")

    random_numb = random.randint(1,100)

# Choose Difficulty
    while True:
        difficulty = input("\033[33mChoose a difficulty. Type 'easy' or 'hard': \033[0m").lower()
        if difficulty == "easy":
            attempts = 10
            print(f"\033[32mYou'll have {attempts} attempts to guess the number. Good Luck!\033[0m")  # Green
            break
        elif difficulty == "hard":
            attempts = 5
            print(f"\033[31mYou'll have {attempts} attempts to guess the number. Good Luck!\033[0m")  # Red
            break
        else:
            print("\033[31mInvalid input. Please type again.\033[0m")


    end_game = False
    while not end_game:
        if attempts > 0:
            guess = int(input("Make a Guess: "))
            if guess > random_numb:
                attempts -= 1
                print(f"Too hight. Guess again.\nYou have {attempts} attempts left.")
            elif guess < random_numb:
                attempts -= 1
                print(f"Too low. Guess again.\nYou have {attempts} attempts left.") 
            else:
                print(win_ascii)
                print(f"You got it, the correct answer was {random_numb}. Congratulations !")
                end_game = True
        else:
            print(loose_ascii)
            print(f"The correct number was {random_numb}")
            print("You've run out of guesses. You loose...")
            end_game = True       

    while end_game:
        restart = input("Would you like to play again? Type 'y' for Yes or 'n' for No: ").lower()

        if restart == 'y':
            end_game = False
            start_game()
        elif restart == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input, please type 'y' for Yes or 'n' for No: ")           


start_game()            