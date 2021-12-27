import random
import time


class Games():

  # GAME 1: Dice roll
  def dice_roll():
    Games.loading("Rolling Dice 1...")
    rand_num = random.randint(1,6)
    print(f"Dice 1: {rand_num}\n")

    Games.loading("Rolling Dice 2...")
    rand_num2 = random.randint(1,6)
    print(f"Dice 2: {rand_num2}\n")

    Games.loading("Calculating total...")
    total = rand_num + rand_num2
    print(f"Roll total: {total}\n")
    Games.loading("...")
    return total


  # GAME 2: Guess the number
  def guess_number():
    Games.loading("Choosing a random number between 1 and 20...")
    randomNum = random.randint(1, 20)
    guessCount = 0

    while guessCount < 5:
      Games.loading(f"You have {5 - guessCount} guesses remaining...")
      userInput = int(input("What's your guess? "))
      if userInput > 50 or userInput < 1:
        Games.loading("Please provide a number between 1 and 20...")
      else:
        if userInput == randomNum:
          Games.loading(f"You guessed CORRECT! The number was {randomNum}")
          return randomNum
        else:
          Games.loading(f"You guess is wrong! Please try again")
          guessCount += 1
      
    Games.loading("You have used all your guesses. Better luck next time!")
    return randomNum
      

  # Loading text with 1 sec delay
  def loading(text):
    print(text)
    time.sleep(1)

# end class


# CLI MENU
gameOn = True

while gameOn:

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
    Games.loading("Exiting...")
    gameOn = False
  elif user_resp < 0 or user_resp >= 3:
    Games.loading("Please select 1 or 0")