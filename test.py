import unittest
from main import Games

class Test(unittest.TestCase):
    def testDiceRollGame(self):
        self.assertTrue(2 <= Games.dice_roll() <= 12)

    def testNumberGuessGame(self):
        self.assertTrue(1 <= Games.guess_number() <= 20)

if __name__ == '__main__':
    unittest.main()