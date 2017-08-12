# ============================================================================ #
# Prufuskrá fyrir hangman.py                                                   #
#                                                                              #
# Oddur Vilhjálmsson  13. febrúar 2015                                         #
# ============================================================================ #

import random
import unittest
from hangman import *

class TestHangmanFunctions(unittest.TestCase):

    def test_firstHint(self):
        word = 'testphrase'
        hint = firstHint(word)
        self.assertEqual(hint, '----------')

    def test_newHint(self):
        word = 'testphrase'
        letter = 't'
        oldhint = '-e-----a-e'
        hint = newHint(letter,word,oldhint)
        self.assertEqual(hint, 'te-t---a-e')

    def test_hang(self):
        word = 'testphrase'
        letter1 = 't'
        letter2 = 'c'
        lives = 5
        lives = hang(word,letter1,lives)
        self.assertEqual(lives, 5)
        lives = hang(word,letter2,lives)
        self.assertEqual(lives, 4)

    def test_guessString(self):
        guess = 'b'
        oldstring = '  a c'
        newstring = guessString(guess, oldstring)
        self.assertEqual(newstring, '  a b c')

    def test_hasWon(self):
        hint1 = 'testphrase'
        hint2 = '-e-----a-e'
        self.assertTrue(hasWon(hint1))
        self.assertFalse(hasWon(hint2))

    def test_score(self):
        hint1 = 'testphrase'
        hint2 = '-e-----a-e'
        self.assertEqual(score(hint1), 1)
        self.assertEqual(score(hint2), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)