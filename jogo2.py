from random import randrange


mapa = [
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','',''],
['','','','','','','','','','']
]

def smap():
    for a in range(0,10):
        print('Vida:',vida)
        print(str(mapa[a]).replace(', ','|').replace("'", " ") )

vida = 3

posXboneco = randrange(0,10)
posYboneco = randrange(0,10)

posXprincess = randrange(0,10)
posYprincess = randrange(0,10)
while posXprincess == posXboneco or posYprincess == posXboneco:
    posXprincess = randrange(0,10)
    posYprincess = randrange(0,10)
