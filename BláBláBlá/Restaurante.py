for a in range(0,5):
    print(a)
lasanha = 40
strogonoff = 20
rattatuile = 80
hamburguer = 15
coxinha = 5
marmita = 15
bolo = 3
sorvete = 5
torta = 4

total = 0


def cardapio():
    print("|=========================================|")
    print("|              [Restaurante]              |")
    print("|=========================================|")
    print('|                 Cardápio                |')
    print("|                                         |")
    print("|  1- Pizza [R$35.00]                     |")
    print("|  2- Lasanha [R$40.00]                   |")
    print("|  3- Strogonoff [R$20.00]                |")
    print("|  4- Rattatuile [R$80.00]                |")
    print("|  5- Hamburguer [R$15.00]                |")
    print("|  6- Coxinha [R$5.00]                    |")
    print("|  7- Marmita[R$15.00]                    |")
    print("|  8- Bolo  [R$3.00]                      |")
    print("|  9- Sorvete [R$5.00]                    |")
    print("| 10- Torta [R$4.00]                      |")
    print("|                                         |")
    print("|                                         |")
    print("|_________________________________________|")


cardapiomostrar = input("Digite Menu para mostrar o cardápio: ")
if cardapiomostrar == "Menu" or cardapiomostrar == "menu":
    cardapio()
print("é os guri")
