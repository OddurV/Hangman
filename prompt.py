# ============================================================================ #
# Hengimaður - prompt.py                                                       #
#                                                                              #
# Tillaga að lausn á hópverkefni 1 í Þróun Hugbúnaðar A (HBV402G)              #
#                                                                              #
# Oddur Vilhjálmsson  13. febrúar 2015                                         #
# ============================================================================ #

# Listi af hengimannsmyndum á strengjaformi
gallows = [
            '''
            _______
            ||   |
            ||   |
            ||  (_)
            ||  /|\ 
            ||  / \ 
            || _____
            ''',
            '''
            _______
            ||   |
            ||  (_) < HJÁLP!
            ||  /|\ 
            || _/_\_
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||  (_)
            ||  /|\ 
            || _/___
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||  (_)
            ||  /|\ 
            || _____
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||  (_)
            ||  /| 
            || _____
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||  (_)
            ||   | 
            || _____
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||  (_)
            ||     
            || _____
            ||  | |
            ||  | |
            ''',
            '''
            _______
            ||   |
            ||   O  
            ||     
            || _____
            ||  | |
            ||  | |
            '''
            ]

# Notkun: status(gallows, lives, hint, guesses)
# Fyrir : gallows er listi af strengjum sem tákna ascii myndir
#         lives er heiltala, 0 <= lives <= 7
#         hint og guesses eru strengir
# Eftir : strengur nr. lives í gallows hefur verið prentaður
#         hint og guesses hafa verið prentaðir
def status(gallows, lives, hint, guesses):
    print(gallows[lives], '\n', '\n')
    print( '           ', hint, '\n')
    print(guesses, '\n')
    print('Þú átt', lives, 'tilraunir eftir.\n')

# Notkun: reveal(word)
# Fyrir : word er strengur
# Eftir : word hefur verið prentað
def reveal(word):
    print('Orðið var:', word, '\n')

# Notkun: scoreboard(points)
# Fyrir : points er heiltala
# Eftir : points hefur verið prentað
def scoreboard(points):
	print('Þú hefur afhjúpað', points, 'orð.\n')