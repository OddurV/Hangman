# ============================================================================ #
# Hengimaður - hangman.py                                                      #
#                                                                              #
# Tillaga að lausn á hópverkefni 1 í Þróun Hugbúnaðar A (HBV402G)              #
#                                                                              #
# Oddur Vilhjálmsson  13. febrúar 2015                                         #
# ============================================================================ #

import random as rnd
import user
import prompt as p

# Notkun: x = rndWord()
# Fyrir : filename er strengur sem vísar í skrá sem er vistuð í 
#         sömu möppu og þetta fall
# Eftir : Eitt orð úr skránni hefur verið valið af handahófi, 
#         og því skilað með lágstöfum eingöngu.
def rndWord(filename):
    return rnd.choice(list(open(filename))).replace('\n','').lower()
    
# Notkun: x = firstHint(word)
# Fyrir : word er strengur.
# Eftir : x er runa af bandstrikum, jafnlöng og inntakið
def firstHint(word):
    x = len(word)
    hint = ''
    for i in range(0,x):
        hint = hint + '-'
    return hint

# Notkun: x = newHint(letter,word,oldhint)
# Fyrir : letter er einn enskur bókstafur, og er lágstafur
#         word er strengur af lágstöfum sem verið er að giska á
#         oldhint er strengur af sömu lengd og word
# Eftir : búið er að bæta letter inn í oldhint á öllum
#         sömu stöðum og hann kemur fyrir í word
def newHint(letter,word,oldhint):
    hint = ''
    for x in range(0,len(word)):
        if word[x] == letter:
            hint += letter
        else:
            hint += oldhint[x]
    return hint

# Notkun: x = hang(word,letter,lives)
# Fyrir : word er strengur sem verið er að giska á
#         letter er einn enskur bókstafur
#         lives er heiltala, 0 <= lives
# Eftir : ef letter er ekki í word þá hefur lives lækkað um 1
#         ef letter er í word gerist ekkert
def hang(word,letter,lives):
    if letter not in word:
        lives += -1
    return lives

# Notkun: x = guessString(guess, oldstring)
# Fyrir : guess er bókstafur, oldstring er strengur
# Eftir : guess hefur verið stungið inn í oldstring í stafrófsröð
#         og skilað sem x
def guessString(guess, oldstring):
    return ' '.join(sorted(set(oldstring + guess)))

# Notkun: x = hasWon(hint)
# Fyrir : hint er strengur
# Eftir : x er true ef hint inniheldur engin bandstrik, annars false
def hasWon(hint):
    return '-' not in hint

# Notkun: x = score(hint)
# Fyrir : hint er strengur
# Eftir : x = 1 ef hasWon(hint) er satt, annars er x = 0
def score(hint):
    if hasWon(hint):
        return 1
    return 0

# Set þá virkni sem ekki er í föllum inn í main fall
# svo að hægt sé að flytja (import) þessa skrá inn í 
# prufuskrána test_hangman.py án þess að leikurinn 
# sé keyrður sjálfkrafa
if __name__ == '__main__':

    # Upphafsstilli breytur
    points = 0
    play = True

    # Leikjalykkja
    while play == True:
    
        # Upphafsstilli breytur
        lives = 7
        word = rndWord('wordsEn.txt') # wordsEn.txt verður að vera í sömu möppu og hangman.py
        hint = firstHint(word)
        guesses = ' '

        # Sýni stöðuna í byrjun leiks
        p.status(p.gallows, lives, hint, guesses)

        # Lykkja fyrir eitt orð
        while lives > 0 and not hasWon(hint):
            letter = user.guess()                     # Fæ ágiskun frá notanda
            guesses = guessString(letter, guesses)    # Geymi ágiskunina
            lives = hang(word,letter,lives)           # Samanburður við orðið
            hint = newHint(letter,word,hint)          # Uppfæri vísbendinguna
            p.status(p.gallows, lives, hint, guesses) # Sýni stöðuna

        # Sýni orðið og uppfæri stigatöfluna
        p.reveal(word) 
        points += score(hint)
        p.scoreboard(points)

        # Spyr hvort notandinn vilji spila aftur
        play = user.replay(lives)