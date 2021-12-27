import random
numOfGuesses = 1
getRandNum = random.randint(1,100)
#print(getRandNum)

#2N1 - Dice Roll Simulator
def dice_roll():
  rand_num = random.randint(1,6)
  print(f"Dice 1: {rand_num}\n")
  rand_num2 = random.randint(1,6)
  print(f"Dice 2: {rand_num2}\n")
  print(f"Roll total: {rand_num + rand_num2}\n")


#2N1 - Number guesser
def guess_tracker(nog):
  #Checks if win condition is satisfied then restarts game
  global numOfGuesses
  global getRandNum
  if nog == 5:
    print("Aww, perhaps you'll guess it next time.\n")
    numOfGuesses = 1
    getRandNum = getRandNum = random.randint(1,100)
    print("A new number between 1 and 100 has been selected.\n")
  else:
    print(f"You have {5 - nog} guesses remaining.\n")

def number_guesser():
  global numOfGuesses
  userNum = int(input("What's your guess? "))
  if(userNum < 0):
    userNum = abs(userNum)
  elif(userNum == 0):
    print("Please limit your guess between 1 and 100.")
    number_guesser()
  elif(userNum >= 100):
    print("Please limit your guess between 1 and 100.")
    number_guesser()
    
  if(userNum == getRandNum):
    print("Congrats! You guessed correctly!")
  elif(userNum > getRandNum):
    print("You guessed too high.")
    guess_tracker(numOfGuesses)
    numOfGuesses += 1
    number_guesser()
  elif(userNum < getRandNum): 
    print("You guessed too low")
    guess_tracker(numOfGuesses)
    numOfGuesses += 1
    number_guesser()


#2N1 - User Interface
print("Welcome to 2N1. \n")
print("Press [1] for a dice roll.\n")
print("Press [2] for the Number Guess game.\n")

user_resp = int(input("Which would you like to select? "))
if user_resp == 1:
  dice_roll()
elif user_resp == 2:
  print("Welcome to Number Guesser. A number between 1 and 100 has been selected. Try to guess the number in 5 turns or fewer. Good luck! ;) \n")
  number_guesser()
elif user_resp <= 0 or user_resp >= 3:
  print("Please select 1 or 2")
