# Random Number

## Games

### Dice Roll
This method simulates two rolls of a 6-sided dice.
It uses the ```random``` module to independently generate two numbers from 1-6.
The script adds the two totals.

### Guess a Number
This method generates a number from 1-20 using the ```random``` module.
The user has 5 attempts to guess the number.

## Testing
Because we use randomly generated numbers, we are not able to easily test the numbers.
The testing focuses on the conditions of the numbers.
The test for Dice Roll ensures the sum of the two numbers is between 1-12 and the Number Gueser checks if the generated numbers are between 1-20.
