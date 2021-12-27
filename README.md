# Random Number

## Games

### Dice Roll
This method simulates the roll of a 6-sided dice.
It uses the ```random``` module to generate two numbers from 1-6 independently. 
The two totals are then added.

### Guess a Number
This method generates a number from 1-20 using the ```random``` module.
The user has 5 guesses to figure out the number.

## Testing
Because we used randomly generated numbers, we could not easily test the numbers generated.
We used Unit Testing on the conditions of the numbers.
We tested Dice Roll to ensure the sum of the two numbers was between 1-12.
We tested the Number Guesser to ensure the script only generated numbers from 1-20.
