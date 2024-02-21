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
    print("""
    |=========================================|
    |              [Restaurante]              |
    |=========================================|
    |                 Cardápio                |
    |                                         |
    |  1- Pizza [R$35.00]                     |
    |  2- Lasanha [R$40.00]                   |
    |  3- Strogonoff [R$20.00]                |
    |  4- Rattatuile [R$80.00]                |
    |  5- Hamburguer [R$15.00]                |
    |  6- Coxinha [R$5.00]                    |
    |  7- Marmita[R$15.00]                    |
    |  8- Bolo  [R$3.00]                      |
    |  9- Sorvete [R$5.00]                    |
    |  10- Torta [R$4.00]                      |
    |                                         |
    |                                         |
    |_________________________________________|""")


cardapiomostrar = input("Digite Menu para mostrar o cardápio: ")
if cardapiomostrar == "Menu" or cardapiomostrar == "menu":
    cardapio()
print("é os guri")
