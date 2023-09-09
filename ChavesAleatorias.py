from random import randrange

def letras(chave):
    if chave == 1:
        chave = "A"
    elif chave == 2:
        chave = "B"
    elif chave == 3:
        chave = "C"
    elif chave == 4:
        chave = "D"
    elif chave == 5:
        chave = "E"
    elif chave == 6:
        chave = "F"
    elif chave == 7:
        chave = "G"
    elif chave == 8:
        chave = "H"
    elif chave == 9:
        chave = "I"
    elif chave == 10:
        chave = "J"
    elif chave == 11:
        chave = "K"
    elif chave == 12:
        chave = "L"
    elif chave == 13:
        chave = "M"  
    elif chave == 14:
        chave = "N"
    elif chave == 15:
        chave = "O"
    elif chave == 16:
        chave = "P"
    elif chave == 17:
        chave = "Q"
    elif chave == 18:
        chave = "R"
    elif chave == 19:
        chave = "S"
    elif chave == 20:
        chave = "T"
    elif chave == 21:
        chave = "U"
    elif chave == 22:
        chave = "V"
    elif chave == 23:
        chave = "W"
    elif chave == 24:
        chave = "X"
    elif chave == 25:
        chave = "Y"
    elif chave == 26:
        chave = "Z"  
    return chave

def tipo(chavinho):
    tipochave = randrange(1,3)
    if tipochave == 1:
        chavinho = randrange(1,27)
        chavinho = letras(chavinho)
    else:
        chavinho = randrange(1,10)
        chavinho = str(chavinho)
    return chavinho

chave1 = 0
chave2 = 0
chave3 = 0
chave4 = 0
chave5 = 0
chave6 = 0
chave7 = 0
chave8 = 0
chave9 = 0
chave10 = 0

for a in range(0, 10):
    chave1 = tipo(chave1)
    chave2 = tipo(chave2)
    chave3 = tipo(chave3)
    chave4 = tipo(chave4)
    chave5 = tipo(chave5)
    chave6 = tipo(chave6)
    chave7 = tipo(chave7)
    chave8 = tipo(chave8)
    chave9 = tipo(chave9)
    chave10 = tipo(chave10)
    
    chavetotal = chave1+chave2+chave3+chave4+chave5+chave6+chave7+chave8+chave9+chave10
    if a > 0:  
        arquivo = open("chaves.txt", "a")
        arquivo.write("\n")

    arquivo = open("chaves.txt", "a")
    arquivo = arquivo.write(chavetotal)
print("c=============================================ↄ")
print("       Abra o seu repositório do VS Code")
print("c=============================================ↄ")