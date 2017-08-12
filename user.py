# ============================================================================ #
# Hengimaður - user.py                                                         #
#                                                                              #
# Tillaga að lausn á hópverkefni 1 í Þróun Hugbúnaðar A (HBV402G)              #
#                                                                              #
# Oddur Vilhjálmsson  13. febrúar 2015                                         #
# ============================================================================ #

# Notkun: x = guess()
# Fyrir : Ekkert
# Eftir : x hefur tekið gildi bókstafs sem notandi hefur 
#         slegið inn á lyklaborðið
def guess():
    x = input('Giskaðu á bókstaf: ')
    while x == '' or x[0].lower() not in "abcdefghijklmnopqrstuvwxyz'":
        print('Villa, inntak var ekki löglegur bókstafur.\n')
        x = input('Giskaðu á bókstaf: ')
    return x[0].lower()


# Notkun: x = replay(lives)
# Fyrir : lives er heiltala
# Eftir : Notandi hefur verið beðinn um streng
#         Ef fyrsta stak strengsins var j, y eða ef strengurinn var tómur
#         þá er x true, annars False
def replay(lives):
    if lives > 0:
        print('Þú vannst!\n')
    else:
        print('Þú tapaðir.\n')
    x=input('Spila aftur? J/N ')
    return x == '' or x[0].lower() == 'j' or x[0].lower() == 'y'