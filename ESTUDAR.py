import random
def linha():
    print("  |-------------------|")

def jogo():
    print(a1)
    linha()
    print(b1)
    linha()
    print(c1)
    linha()
    print(d1)
    linha()
    print(e1)

def jogolimpo():
    print(a1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    print(b1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    print(c1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    print(d1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    print(e1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))



a = "A |1|2|3|4|5|6|7|8|9|0|"
b = "B |1|2|3|4|5|6|7|8|9|0|"
c = "C |1|2|3|4|5|6|7|8|9|0|"
d = "D |1|2|3|4|5|6|7|8|9|0|"
e = "E |1|2|3|4|5|6|7|8|9|0|"

a1 = a
b1 = b
c1 = c
d1 = d
e1 = e


startlinha_estrela = random.randrange(1,6)
startcoluna_estrela = str(random.randrange(0,10))
startlinha_personagem = random.randrange(1,6)
startcoluna_personagem = str(random.randrange(0,10))

while startlinha_estrela == startlinha_personagem:
        startlinha_estrela = random.randrange(1,6)

print("linha estrela: ",startlinha_estrela)
print("coluna estrela: ",startcoluna_estrela)
print()
print("linha personagem: ",startlinha_personagem)
print("coluna personagem: ",startcoluna_personagem)

#estrela
if startlinha_estrela == 1:
        a1 = a.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 2:
        b1 = b.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 3:
        c1 = c.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 4:
        d1 = d.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 5:
        e1 = e.replace(startcoluna_estrela, "*")

#personagem
if startlinha_personagem == 1:
        a1 = a.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 2:
        b1 = b.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 3:
        c1 = c.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 4:
        d1 = d.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 5:
        e1 = e.replace(startcoluna_personagem, "£")
#tentar colocar o de cima em for


jogo()
jogolimpo()

for a in range(0,999999999999):
        comando  = input("Digite a direção que o personagem irá de se mover: ")
        if comando == "cima" or comando == "Cima":
                cima = int(input(('Quantos passos para cima? ')))
        elif comando == 'baixo' or comando == 'Baixo':
                baixo = int(input(('Quantos passos para baixo? ')))
        elif comando == 'direita' or comando == 'Direita':
                direita = int(input(('Quantos passos para direita? ')))
        elif comando == 'esquerda' or comando == 'Esquerda':
                esquerda = int(input(('Quantos passos para esquerda? ')))
        

#inacabado


