def espaço():
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()


import random
from time import sleep
def linha():
    print("  |-------------------|")



def jogolimpo():
    linha()
    print(a1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(b1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(c1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(d1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()
    print(e1.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," "))
    linha()



        



a = "  |0|1|2|3|4|5|6|7|8|9|"
b = "  |0|1|2|3|4|5|6|7|8|9|"
c = "  |0|1|2|3|4|5|6|7|8|9|"
d = "  |0|1|2|3|4|5|6|7|8|9|"
e = "  |0|1|2|3|4|5|6|7|8|9|"



startlinha_estrela = random.randrange(1,6)
startcoluna_estrela = str(random.randrange(0,10))
startlinha_personagem = random.randrange(1,6)
startcoluna_personagem = str(random.randrange(0,10))

while startlinha_estrela == startlinha_personagem:
        startlinha_estrela = random.randrange(1,6)
while startcoluna_estrela == startcoluna_personagem:
        startcoluna_estrela = str(random.randrange(0,10))

#spawn aleatório

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

a1 = a
b1 = b
c1 = c
d1 = d
e1 = e

#spawn personagem
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

print("Pegue a estrela (*) com seu personagem (£)")

jogolimpo()

#andar
while True:
        if startcoluna_estrela == startcoluna_personagem and startlinha_estrela == startlinha_personagem:
                a1 = a.replace("*","£")
                b1 = b.replace("*","£")
                c1 = c.replace("*","£")
                d1 = d.replace("*","£")
                e1 = e.replace("*","£")
                espaço()
                jogolimpo()
                print()
                linha()
                print("  Você pegou a estrela!")
                linha()
                break
        
        comando  = input("Digite a direção que o personagem irá de se mover: ")
        if comando == "cima" or comando == "Cima":
                cima = int(input(('Quantos passos para cima? ')))
                for andar in range(0,cima):
                        startlinha_personagem = startlinha_personagem - 1
                        if startlinha_personagem < 1:
                                startlinha_personagem = 1
                        if startlinha_personagem == 4:
                                d1 = d.replace(startcoluna_personagem, "£")
                                e1 = e.replace("£",startcoluna_personagem )
                        elif startlinha_personagem == 3:
                                c1 = c.replace(startcoluna_personagem, "£")  
                                d1 = d.replace("£",startcoluna_personagem ) 
                        elif startlinha_personagem == 2:
                                b1 = b.replace(startcoluna_personagem, "£")
                                c1 = c.replace("£",startcoluna_personagem )
                        elif startlinha_personagem == 1:
                                a1 = a.replace(startcoluna_personagem, "£")
                                b1 = b.replace("£",startcoluna_personagem )
                        sleep(1)
                        espaço()
                        jogolimpo()

                
        elif comando == 'baixo' or comando == 'Baixo':
                baixo = int(input(('Quantos passos para baixo? ')))
                for andar in range(0,baixo):
                        startlinha_personagem = startlinha_personagem + 1
                        if startlinha_personagem > 5:
                                startlinha_personagem = 5
                        if startlinha_personagem == 1:
                                a1 = a.replace(startcoluna_personagem, "£")                          
                        elif startlinha_personagem == 2:
                                b1 = b.replace(startcoluna_personagem, "£")
                                a1 = a.replace("£",startcoluna_personagem)
                        elif startlinha_personagem == 3:
                                c1 = c.replace(startcoluna_personagem, "£")
                                b1 = b.replace("£",startcoluna_personagem)
                        elif startlinha_personagem == 4:
                                d1 = d.replace(startcoluna_personagem, "£")
                                c1 = c.replace("£",startcoluna_personagem)
                        elif startlinha_personagem == 5:
                                e1 = e.replace(startcoluna_personagem, "£")
                                d1 = d.replace("£",startcoluna_personagem)
                        sleep(1)
                        espaço()
                        jogolimpo()
                
        elif comando == 'direita' or comando == 'Direita':
                direita = int(input(('Quantos passos para direita? ')))
                for andar in range(0,direita):
                        startcoluna_personagem = int(startcoluna_personagem) + 1
                        if int(startcoluna_personagem) > 9:
                                startcoluna_personagem = "9"
                        startcoluna_personagem = str(startcoluna_personagem)
                        if startlinha_personagem == 1:
                                a1 = a.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 2:
                                b1 = b.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 3:
                                c1 = c.replace(startcoluna_personagem,"£")
                                
                        elif startlinha_personagem == 4:
                                d1 = d.replace(startcoluna_personagem,"£")
                               
                        elif startlinha_personagem == 5:
                                e1 = e.replace(startcoluna_personagem,"£")
                                
                        sleep(1)
                        espaço()
                        jogolimpo()
                
        elif comando == 'esquerda' or comando == 'Esquerda':
                esquerda = int(input(('Quantos passos para esquerda? ')))
                for andar in range(0,esquerda):
                        startcoluna_personagem = int(startcoluna_personagem) - 1
                        startcoluna_personagem = str(startcoluna_personagem)
                        if startlinha_personagem == 1:
                                if int(startcoluna_personagem) < 0:
                                        startcoluna_personagem = "0"
                                a1 = a.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 2:
                                if int(startcoluna_personagem) < 0:
                                        startcoluna_personagem = "0"
                                b1 = b.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 3:
                                if int(startcoluna_personagem) < 0:
                                        startcoluna_personagem = "0"
                                c1 = c.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 4:
                                if int(startcoluna_personagem) < 0:
                                        startcoluna_personagem = "0"
                                d1 = d.replace(startcoluna_personagem,"£")
                        elif startlinha_personagem == 5:
                                if int(startcoluna_personagem) < 0:
                                        startcoluna_personagem = "0"
                                e1 = e.replace(startcoluna_personagem,"£")
                        sleep(1)
                        espaço()
                        jogolimpo()
        elif comando in ["fechar", "Fechar", "sair", "Sair"]:
                break
        

        