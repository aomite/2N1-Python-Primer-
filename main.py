'''
Main.py has two games that users can choose from and play. The first is
dice roll and the second is guess the number. Enjoy!
'''
import random
import time

def loading(text):
    '''
    Loads text with a one second delay!
    '''
    print(text)
    time.sleep(1)

class Games():
    '''
    The games class creates an class capable of two games: dice roll and
    guess the number
    '''
    @staticmethod
    def dice_roll():
        '''
        Game #1: Dice Roll!
        '''
        loading("Rolling Dice 1...")
        rand_num = random.randint(1,6)
        print(f"Dice 1: {rand_num}\n")

        loading("Rolling Dice 2...")
        rand_num2 = random.randint(1,6)
        print(f"Dice 2: {rand_num2}\n")

        loading("Calculating total...")
        total = rand_num + rand_num2
        print(f"Roll total: {total}\n")
        loading("...")
        return total

    @staticmethod
    def guess_number():
        '''
        Game #2: Guess the number!
        '''
        loading("Choosing a random number between 1 and 20...")
        random_num = random.randint(1, 20)
        guess_count = 0

        while guess_count < 5:
            loading(f"You have {5 - guess_count} guesses remaining...")
            user_input = int(input("What's your guess? "))
            if user_input > 20 or user_input < 1:
                loading("Please provide a number between 1 and 20...")
            else:
                if user_input != random_num:
                    loading("You guess is wrong! Please try again")
                    guess_count += 1
                else:
                    loading(f"You guessed CORRECT! The number was {random_num}")
                    return random_num
        loading("You have used all your guesses. Better luck next time!")
        return random_num
# end class


# CLI MENU
GAME_ON = True

while GAME_ON:

    #User Interface
    print("Welcome to 2N1. \n")
    print("Press [1] for a dice roll.\n")
    print("Press [2] for the Number Guess game.\n")
    print("Press [0] to exit")

    user_resp = int(input("Which would you like to select? "))
    if user_resp == 1:
        Games.dice_roll()
    elif user_resp == 2:
        Games.guess_number()
    elif user_resp == 0:
        loading("Exiting...")
        GAME_ON = False
    elif user_resp < 0 or user_resp >= 3:
        loading("Please select 1, 2 or 0")
