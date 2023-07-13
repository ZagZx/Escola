import random
def linha():
    print("  |--------------------|")

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


a = "A |1|2|3|4|5|6|7|8|9|10|"
b = "B |1|2|3|4|5|6|7|8|9|10|"
c = "C |1|2|3|4|5|6|7|8|9|10|"
d = "D |1|2|3|4|5|6|7|8|9|10|"
e = "E |1|2|3|4|5|6|7|8|9|10|"

startlinha_estrela = random.randrange(1,6)
startcoluna_estrela = str(random.randrange(1,11))
startlinha_personagem = random.randrange(1,6)
startcoluna_personagem = str(random.randrange(1,11))

print("linha estrela: ",startlinha_estrela)
print("coluna estrela: ",startcoluna_estrela)
print()
print("linha personagem: ",startlinha_personagem)
print("coluna personagem: ",startcoluna_personagem)

#estrela
if startlinha_estrela == 1:
    if startcoluna_estrela == "10":
        a = a.replace(startcoluna_estrela, "* ")
    else:
        a = a.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 2:
    if startcoluna_estrela == "10":
        b = b.replace(startcoluna_estrela, "* ")
    else:
        b = b.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 3:
    if startcoluna_estrela == "10":
        c = c.replace(startcoluna_estrela, "* ")
    else:
        c = c.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 4:
    if startcoluna_estrela == "10":
        d = d.replace(startcoluna_estrela, "* ")
    else:
        d = d.replace(startcoluna_estrela, "*")


elif startlinha_estrela == 5:
    if startcoluna_estrela == "10":
        e = e.replace(startcoluna_estrela, "* ")
    else:
        e = e.replace(startcoluna_estrela, "*")

#personagem
if startlinha_personagem == 1:
    if startcoluna_personagem == "10":
        a = a.replace(startcoluna_personagem, "£ ")
    else:
        a = a.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 2:
    if startcoluna_personagem == "10":
        b = b.replace(startcoluna_personagem, "£ ")
    else:
        b = b.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 3:
    if startcoluna_personagem == "10":
        c = c.replace(startcoluna_personagem, "£ ")
    else:
        c = c.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 4:
    if startcoluna_personagem == "10":
        d = d.replace(startcoluna_personagem, "£ ")
    else:
        d = d.replace(startcoluna_personagem, "£")


elif startlinha_personagem == 5:
    if startcoluna_personagem == "10":
        e = e.replace(startcoluna_personagem, "£ ")
    else:
        e = e.replace(startcoluna_personagem, "£")
#tentar colocar o de cima em for

a = a.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," ")
b = b.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," ")
c = c.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," ")
d = d.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," ")
e = e.replace("1"," ").replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ").replace("6"," ").replace("7"," ").replace("8"," ").replace("9"," ").replace("0"," ")

jogo()

#for a in range(0,999999999999):
 #   comando  = input("Digite a direção que o personagem irá de se mover: ")
    #if comando == "cima":
#inacabado


