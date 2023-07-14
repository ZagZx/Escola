import random
from time import sleep
def linha():
    print("  |-------------------|")

def jogo():
    print(a)
    linha()
    print(b)
    linha()
    print(c)
    linha()
    print(d)
    linha()
    print(e)

def jogolimpo():
    print(a.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(b.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(c.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(d.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(e.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))



#arrumar a troca de variavel


        



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


startlinha_estrela = 1
startcoluna_estrela = "5"
startlinha_personagem = 5
startcoluna_personagem = "1"

random.randrange(1,6)
str(random.randrange(0,10))

while startlinha_estrela == startlinha_personagem:
        startlinha_estrela = random.randrange(1,6)

print("linha estrela: ",startlinha_estrela)
print("coluna estrela: ",startcoluna_estrela)
print()
print("linha personagem: ",startlinha_personagem)
print("coluna personagem: ",startcoluna_personagem)

#estrela
if startlinha_estrela == 1:
        a = a.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 2:
        b = b.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 3:
        c = c.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 4:
        d = d.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 5:
        e = e.replace(startcoluna_estrela, "*")

#personagem
if startlinha_personagem == 1:
        a = a.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 2:
        b = b.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 3:
        c = c.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 4:
        d = d.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 5:
        e = e.replace(startcoluna_personagem, "£")
#tentar colocar o de cima em for


jogo()

while True:
        comando  = input("Digite a direção que o personagem irá de se mover: ")
        if comando == "cima" or comando == "Cima":
                cima = int(input(('Quantos passos para cima? ')))
                for andar in range(0,cima):
                        startlinha_personagem = startlinha_personagem - 1
                        if startlinha_personagem == 4:
                                d = d.replace(startcoluna_personagem, "£")
                        
                        elif startlinha_personagem == 3:
                                c = c.replace(startcoluna_personagem, "£")
                                
                        elif startlinha_personagem == 2:
                                b = b.replace(startcoluna_personagem, "£")

                        elif startlinha_personagem == 1:
                                a = a.replace(startcoluna_personagem, "£")
                
                
                        
                        
                        

        elif comando == 'baixo' or comando == 'Baixo':
                baixo = int(input(('Quantos passos para baixo? ')))
                for andar in range(0,baixo):
                        startlinha_personagem = startlinha_personagem + 1
                        if startlinha_personagem == 1:
                                a = a.replace(startcoluna_personagem, "£")
                                
                        elif startlinha_personagem == 2:
                                b = b.replace(startcoluna_personagem, "£")
                                
                        elif startlinha_personagem == 3:
                                c = c.replace(startcoluna_personagem, "£")
                                
                        elif startlinha_personagem == 4:
                                d = d.replace(startcoluna_personagem, "£")
                        elif startlinha_personagem == 5:
                                e = e.replace(startcoluna_personagem, "£")
                
                

        elif comando == 'direita' or comando == 'Direita':
                direita = int(input(('Quantos passos para direita? ')))
                for andar in range(0,direita):
                        startcoluna_personagem = int(startcoluna_personagem) + 1
                        startcoluna_personagem = str(startcoluna_personagem)
                        if startlinha_personagem == 1:
                                a = a.replace(startcoluna_personagem,"£")
                                if int(startcoluna_personagem) > 9:
                                        a = a.replace("0", "£")
                        elif startlinha_personagem == 2:
                                b = b.replace(startcoluna_personagem,"£")
                                if int(startcoluna_personagem) >= 10:
                                        b = b.replace("0", "£")
                        elif startlinha_personagem == 3:
                                c = c.replace(startcoluna_personagem,"£")
                                if int(startcoluna_personagem) >= 10:
                                        c = c.replace("0", "£")
                        elif startlinha_personagem == 4:
                                d = d.replace(startcoluna_personagem,"£")
                                if int(startcoluna_personagem) >= 10:
                                        d = d.replace("0", "£")
                        elif startlinha_personagem == 5:
                                e = e.replace(startcoluna_personagem,"£")
                                if int(startcoluna_personagem) >= 10:
                                        e = e.replace("0", "£")
                                
                
                
        elif comando == 'esquerda' or comando == 'Esquerda':
                esquerda = int(input(('Quantos passos para esquerda? ')))
                for andar in range(0,esquerda):
                        startcoluna_personagem = int(startcoluna_personagem) - 1
                        startcoluna_personagem = str(startcoluna_personagem)
                        if startlinha_personagem == 1:
                                a = a.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 2:
                                b = b.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 3:
                                c = c.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 4:
                                d = d.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 5:
                                e = e.replace(startcoluna_personagem,"£")
        jogolimpo()
